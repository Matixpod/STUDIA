"use client";
import React from "react";
import Navigation from "./Navigation";
import HeroSection from "./HeroSection";
import TrendingMovies from "./TrendingMovies";
import AboutSection from "./AboutSection";
import CategoriesSection from "./CategoriesSection";
import styles from "./styles/MovieRateApp.module.css";

function MovieRateApp() {
  return (
    <div className={styles.container}>
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

export default MovieRateApp;
