import React, { useState } from 'react';

const App = (): JSX.Element => {
    const [click, setClick] = useState(false);
    const [name, setName] = useState("World");
    return (
        <div>{click
            ? <div>
                <h1>💖 Hello {name}!</h1>
                <p>Welcome to your Electron application.</p>
                <form>
                    <input id="input-name" type="text" onChange={(event) => setName(event.target.value)} />
                </form>
            </div>
            : <button onClick={() => setClick(true)}>
                Click me
            </button>
        }
        </div>

    );
};

export default App;