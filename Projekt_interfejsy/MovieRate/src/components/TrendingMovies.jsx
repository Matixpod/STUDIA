import React from "react";
import MovieCard from "./MovieCard";
import styles from "./styles/TrendingMovies.module.css";

function TrendingMovies() {
  const trendingMovies = [
    {
      title: "The Last Chapter",
      rating: "4.8",
      genre: "Drama",
      imageUrl: "https://placehold.co/400x600",
    },
    {
      title: "Beyond Tomorrow",
      rating: "4.5",
      genre: "Sci-Fi",
      imageUrl: "https://placehold.co/400x600",
    },
    {
      title: "Laugh Out Loud",
      rating: "4.7",
      genre: "Comedy",
      imageUrl: "https://placehold.co/400x600",
    },
  ];

  return (
    <section className={styles.trendingSection}>
      <h2 className={styles.sectionTitle}>Trending Now</h2>
      <div className={styles.moviesGrid}>
        {trendingMovies.map((movie, index) => (
          <MovieCard
            key={index}
            title={movie.title}
            rating={movie.rating}
            genre={movie.genre}
            imageUrl={movie.imageUrl}
          />
        ))}
      </div>
    </section>
  );
}

export default TrendingMovies;
