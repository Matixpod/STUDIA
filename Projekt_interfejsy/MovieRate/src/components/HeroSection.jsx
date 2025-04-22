"use client";
import React, { useState } from "react";
import styles from "./styles/HeroSection.module.css";

function HeroSection() {
  const [searchQuery, setSearchQuery] = useState("");

  const handleSearchChange = (event) => {
    setSearchQuery(event.target.value);
  };

  return (
    <section className={styles.heroSection}>
      <img
        src="https://placehold.co/1920x600"
        alt="Hero background"
        className={styles.heroImage}
      />
      <div className={styles.heroContent}>
        <h2 className={styles.heroTitle}>
          Discover & Rate Your Favorite Movies
        </h2>
        <div className={styles.searchContainer}>
          <input
            type="text"
            className={styles.searchInput}
            placeholder="Search for movies or series..."
            value={searchQuery}
            onChange={handleSearchChange}
            aria-label="Search movies and series"
          />
        </div>
      </div>
    </section>
  );
}

export default HeroSection;
