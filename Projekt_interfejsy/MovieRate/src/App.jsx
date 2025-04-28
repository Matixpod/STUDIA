// src/App.jsx
import Navigation from './components/Navigation';
import HeroSection from './components/HeroSection';
import TrendingMovies from './components/TrendingMovies';
import AboutSection from './components/AboutSection';
import CategoriesSection from './components/CategoriesSection';
import './App.css';

function App() {
  return (
    <div className="App">
      <Navigation />
      <main>
        <HeroSection />
        <TrendingMovies />
        <AboutSection />
        <CategoriesSection />
      </main>
    </div>
  );
}

export default App;