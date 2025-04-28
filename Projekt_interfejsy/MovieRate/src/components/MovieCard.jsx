import React from "react";
import styles from "./styles/MovieCard.module.css";

function MovieCard({ title, rating, genre, imageUrl }) {
  return (
    <article className={styles.movieCard}>
      <img src={imageUrl} alt={title} className={styles.movieImage} />
      <div className={styles.movieInfo}>
        <h3 className={styles.movieTitle}>{title}</h3>
        <div className={styles.movieMeta}>
          <span className={styles.rating}>★ {rating}</span>
          <span className={styles.genre}>{genre}</span>
        </div>
      </div>
    </article>
  );
}

export default MovieCard;
