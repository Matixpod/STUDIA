import { useState, useEffect } from 'react'
import Papa from 'papaparse'

const useMoviesData = () => {
  const [movies, setMovies] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Załaduj plik CSV z folderu public
    Papa.parse('/movies.csv', {  // lub './movies.csv' jeśli pierwsza opcja nie działa
      download: true,
      header: true,
      complete: (results) => {
        // Przekształć dane do naszego formatu
        const formattedMovies = results.data
          .filter(movie => movie.Series_Title) // Filtruj puste wiersze
          .map((movie, index) => ({
            id: index + 1,
            title: `${movie.Series_Title} (${movie.Released_Year})`,
            subtitle: `feat. ${movie.Director}`,
            rating: parseFloat(movie.IMDB_Rating) / 2, // IMDB ma skalę 0-10, my używamy 0-5
            reviews: `${(parseInt(movie.No_of_Votes) / 1000).toFixed(1)}k recenzji`,
            image: movie.Poster_Link,
            genre: movie.Genre,
            runtime: movie.Runtime,
            overview: movie.Overview,
            stars: [movie.Star1, movie.Star2, movie.Star3, movie.Star4].filter(star => star),
            gross: movie.Gross
          }))
        
        setMovies(formattedMovies)
        setLoading(false)
      },
      error: (error) => {
        console.error('Error loading CSV:', error)
        setLoading(false)
      }
    })
  }, [])

  return { movies, loading }
}

export default useMoviesData