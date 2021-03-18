import React from 'react';
import {Form, Input, Button} from 'antd';
import './styles.scss';

type DetectCateforyFormType = {
    onSubmit: (data: string[]) => void
    onClearResult: () => void
}

export function DetectCateforyForm ({
    onSubmit,
    onClearResult
}: DetectCateforyFormType) {

    const submitHandler = (data: any) => {
        if (data) {
            onSubmit(data.url.split('\n').filter(Boolean));
        }
    };

    return (
        <>
            <Form
                className='detect-category-form'
                onFinish={submitHandler}
            >
                <Form.Item 
                    name='url'
                    label={
                        <>
                            <span>Url</span>
                            <span className='sub-tt'>(Press Enter in case you want to add many urls)</span>
                        </>
                    }
                    className='url-field'
                    rules={[{ required: true, message: 'Please input url!' }]}
                >
                    <Input.TextArea rows={5} size='large' allowClear/>
                </Form.Item >
                <Form.Item>
                    <Button type="primary" htmlType="submit" className='btn-submit'>
                        Submit
                    </Button>
                    <Button className='btn-clear' onClick={onClearResult}>
                        Clear Result
                    </Button>
                </Form.Item>
            </Form>
        </>
    );
}