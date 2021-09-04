import React, { useState } from 'react';

const App = (): JSX.Element => {
    const [click, setClick] = useState(false);
    return (
        <div>{click
            ? <div>
                <h1>💖 Hello World!</h1>
                <p>Welcome to your Electron application.</p>
            </div>
            : <button onClick={() => setClick(true)}>
                Click me
            </button>
        }
        </div>

    );
};

export default App;