import React, { useEffect, useMemo, useState } from 'react';
import {CanvasJSChart} from 'canvasjs-react-charts';
import { DetectResultItem } from 'model';
import { notification, Spin } from 'antd';
import { LoadingOutlined } from '@ant-design/icons';
import './style.scss';
import { DataAccess } from 'access';

type ResultItemType = {
    url: string
}

export function ResultItem({
    url,
}: ResultItemType) {
    const [loading, setLoading] = useState(false);
    const [data, setData] = useState<DetectResultItem[]>([]);

    useEffect(() => {
        setLoading(true);
        DataAccess.Post('api/v1.0/detect_category',{
            url: url
        }).then(res => {
            setData(res?.data?.category ?? []);
            setLoading(false);
            notification.success({
                message: 'Detect sucessfully!'
            });
        }).catch(e => {
            notification.error({
                message: 'Sorry, something went wrong!'
            });
            setLoading(false);
        });
    },[url]);
    const options = useMemo(() => {
        return {
            animationEnabled: true,
            axisX:{
                interval: 1,
            },
            axisY: {
            },
            axisY2: {
                maximum: 100,
                gridDashType: 'dot',
            },
            data: [
                {
                    axisYType: 'secondary',
                    type: 'bar',
                    color: '#40a9ff',
                    dataPoints: data.map(item => {
                        return {
                            label: item.label.split('_').join(' '),
                            y: item.y * 100
                        };
                    }), 
                }
            ]
        };
    },[data]);
    return (
        <div className='result-item'>
            <div className='chart'>
                {loading ? 
                    <Spin indicator={<LoadingOutlined style={{ fontSize: 50 }} spin />} /> : <CanvasJSChart options={options}/>}
            </div>
            <p className='title'>Url:
                <i className='url'>{url}</i>
            </p>
        </div>
    );
}