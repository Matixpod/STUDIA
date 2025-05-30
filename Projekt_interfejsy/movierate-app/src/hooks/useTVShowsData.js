import { useState, useEffect } from 'react'
import Papa from 'papaparse'

const useTVShowsData = () => {
  const [tvShows, setTVShows] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Załaduj plik CSV z folderu public
    Papa.parse('/tvshows.csv', { // <- upewnij się że nazwa pliku jest poprawna
      download: true,
      header: true,
      complete: (results) => {
        // Przekształć dane do naszego formatu
        const formattedShows = results.data
          .filter(show => show.Series_Title) // Filtruj puste wiersze
          .map((show, index) => ({
            id: index + 1,
            title: show.Series_Title,
            subtitle: `Czas trwania: ${show.Runtime_of_Series}`,
            episodeRuntime: show.Runtime_of_Episodes,
            rating: parseFloat(show.IMDB_Rating) / 2, // IMDB ma skalę 0-10, my używamy 0-5
            reviews: `${(parseInt(show.No_of_Votes) / 1000).toFixed(1)}k recenzji`,
            image: show.Poster_Link,
            genre: show.Genre,
            certificate: show.Certificate,
            overview: show.Overview,
            stars: [show.Star1, show.Star2, show.Star3, show.Star4].filter(star => star)
          }))
          .sort((a, b) => b.rating - a.rating) // Sortuj według oceny
        
        setTVShows(formattedShows)
        setLoading(false)
      },
      error: (error) => {
        console.error('Error loading TV Shows CSV:', error)
        setLoading(false)
      }
    })
  }, [])

  return { tvShows, loading }
}

export default useTVShowsData