import React from 'react';

const SubmitButton = ({children, ...props}) => {

    return (
        <button {...props}>
            {children}
        </button>
    )
}

export default SubmitButton;