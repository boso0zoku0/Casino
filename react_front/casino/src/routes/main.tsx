import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import GameStart from '../../src/components/app/game.tsx';
import RegistrationForm from '../../src/components/app/auth.tsx';


const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path="/first-page" element={<RegistrationForm />} />
        <Route path="/second-page" element={<GameStart />} />
      </Routes>
    </Router>
  );
};

export default AppRoutes;