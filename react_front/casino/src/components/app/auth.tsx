import React, {useState} from 'react';
import axios from 'axios';

const RegistrationForm = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault(); // Предотвращаем перезагрузку страницы

    try {
      const response = await axios.post(
        'http://127.0.0.1:8000/auth/registrations/',
        {username, password, email}, // Данные отправляются в формате JSON
        {
          headers: {
            'Content-Type': 'application/json', // Новый заголовок
          },
        }
      );

      setMessage(`Регистрация прошла успешно! ${response.data.message || ''}`);
    } catch (error) {
      let errorDetail = '';
      if (error.response && error.response.data.detail) {
        errorDetail = typeof error.response.data.detail === 'string' ?
          error.response.data.detail :
          JSON.stringify(error.response.data.detail);
      }
      setMessage(`Ошибка регистрации: ${errorDetail || error.message}`);
    }
  };

  return (
    <>
      <img src={"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOHJNyiVkFRRlC2xZTXedtnnAJ0PqSU2Jp3A&s"}
           alt={'casino'} width={'300'} height={'300'}/>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Username:</label><br/>
        <input type="text" id="username" value={username} onChange={(e) => setUsername(e.target.value)}
               required/><br/><br/>

        <label htmlFor="password">Password:</label><br/>
        <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)}
               required/><br/><br/>

        <label htmlFor="email">Email:</label><br/>
        <input type="email" id="email" value={email} onChange={(e) => setEmail(e.target.value)} required/><br/><br/>

        <button type="submit">Зарегистрироваться</button>
        <p style={{color: message.includes('Ошибка') ? 'red' : 'green'}}>{message}</p>
      </form>
    </>
  );
};

export default RegistrationForm;