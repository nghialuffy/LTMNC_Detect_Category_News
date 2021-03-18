import React, { useState } from 'react';
import './App.scss';
import { DetectCateforyForm, ResultItem } from './components';

function App() {
    const [listResult, setListResult] = useState<string[]>([]);
    const onSubmit = async (listUrl: string []) => {
        setListResult(listUrl);
    };

    return (
        <div className="App">
            <h1 className='web-title'>Detect category of articles</h1>
            <DetectCateforyForm onSubmit={onSubmit} onClearResult={() => setListResult([])}/>
            {listResult?.length !== 0 && 
                <div className='result'>
                    <div className='result-header'>
                        <div className='title'>
                            Result
                        </div>
                        
                    </div>
                    <hr/>
                    <div className='list-result'>
                        {listResult.map((url) => <ResultItem url={url} key={url}/>)}
                    </div>
                </div>
            }
        </div>
    );
}

export default App;
