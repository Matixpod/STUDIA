import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'
import Header from './components/Header'
import HomePage from './pages/HomePage'
import TVShowsPage from './pages/TVShowsPage'
import MoviesPage from './pages/MoviesPage'

function App() {
  return (
    <Router>
      <div className="app">
        <Header />
          <Routes>
            <Route path="/" element={<HomePage />} />           {/* Strona główna */}
            <Route path="/tv-shows" element={<TVShowsPage />} /> {/* Strona TV Shows */}
            <Route path="/movies" element={<MoviesPage />} />     {/* Strona Movies */}
          </Routes>
      </div>
    </Router>
  )
}

export default App