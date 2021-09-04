import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App';

// Say something
console.log('Renderer execution started');

const mainElement = document.createElement('div');
document.body.appendChild(mainElement);

ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    mainElement,
);
