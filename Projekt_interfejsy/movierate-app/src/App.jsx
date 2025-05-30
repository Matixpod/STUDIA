import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'
import { SettingsProvider } from './context/SettingsContext'
import { OrdersProvider } from './context/OrdersContext'
import Header from './components/Header'
import HomePage from './pages/HomePage'
import TVShowsPage from './pages/TVShowsPage'
import MoviesPage from './pages/MoviesPage'
import DetailPage from './pages/DetailPage'
import OrderReviewPage from './pages/OrderReviewPage'
import ReviewMarketplace from './pages/ReviewMarketplace'

function App() {
  return (
    <SettingsProvider>
      <OrdersProvider>
        <Router>
          <div className="app">
            <Header />
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/tv-shows" element={<TVShowsPage />} />
              <Route path="/movies" element={<MoviesPage />} />
              <Route path="/movie/:id" element={<DetailPage type="movie" />} />
              <Route path="/tv-show/:id" element={<DetailPage type="tvshow" />} />
              <Route path="/order-review" element={<OrderReviewPage />} />
              <Route path="/review-marketplace" element={<ReviewMarketplace />} />
            </Routes>
          </div>
        </Router>
      </OrdersProvider>
    </SettingsProvider>
  )
}

export default App