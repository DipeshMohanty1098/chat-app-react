import {useState, useEffect} from 'react';
import {useHistory} from 'react-router-dom';


const Name = () => {
    const [name, setName] = useState('')
    const [error, setError] = useState('')
    const history = useHistory();

    const handleClick = () => {
        //a little form validation
        if (name == ''){
            setError('Please enter a valid name :)')
        } else {
        //if everything is handy dandy, go ahead and push the user to the chat page
        localStorage.setItem( 'Name', name );
        history.push("/chat/chatRoom=" + "chatRoom1");
        }
    }

    useEffect(() => {
        //if the user is already logged in and trying to go back to the login page, redirect to the chat page
        if (localStorage.getItem('Name') != null){
            history.push("/chat/chatRoom=" + "chatRoom1")
        }
    }, [])

    return (
        <div className="inputName">
        <h3>Chat App :D</h3>
        <form className="nameForm">
        <input className = "center" type="text" required value={name} onChange={(e) => setName(e.target.value)} placeholder="Enter your name"/>
        </form>
        <p style={{color: "red"}}>{error}</p>
        <button className="center" onClick={handleClick}>Start Chatting!</button>
        </div>
    )
}

export default Name;
