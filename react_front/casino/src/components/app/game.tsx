import styles from '../../styles/app.game.module.css';
import React, {useState} from 'react';
import axios from 'axios'; // Используем библиотеку для отправки AJAX-запросов

export default function GameStart() {
  const [bet, setBet] = useState(''); // Хранит введённую ставку
  const [result, setResult] = useState(''); // Сохраняет результат после отправки ставки
  const [isLoading, setIsLoading] = useState(false); // Индикатор загрузки


  const handleClick = async () => {
    setIsLoading(true); // Включаем индикатор загрузки
    try {
      const response = await axios.post(`http://127.0.0.1:8000/roulette/join?bet=${bet}`, {
        bet: parseInt(bet),
      }, {withCredentials: true});

      // Получаем ответ от сервера и показываем результат
      setResult(response.data.result || 'Unknown');
    } catch (error) {
      // Обрабатываем возможную ошибку (например, если ставка отрицательная или превышена лимит)
      setResult('An error occurred while processing your bet.');
    } finally {
      setIsLoading(false); // Завершаем загрузку
    }
  };

  return (
    <div className="container">
      <h2>Try Your Luck Here!</h2>
      <div>
        <input
          type="number"
          placeholder="Enter your bet amount here..."
          value={bet}
          onChange={(e) => setBet(e.target.value)}
          disabled={isLoading} // Блокируем ввод, пока идёт обработка
        />
        <button onClick={handleClick} disabled={isLoading}>
          Place Bet
        </button>
      </div>
      {result && <p>{result}</p>}
    </div>
  );
}