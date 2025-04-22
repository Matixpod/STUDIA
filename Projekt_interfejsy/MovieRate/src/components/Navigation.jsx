"use client";
import React from "react";
import styles from "./styles/Navigation.module.css";

function Navigation() {
  return (
    <nav className={styles.navbar}>
      <div className={styles.navContent}>
        <h1 className={styles.logo}>MovieRate</h1>
        <div className={styles.navLinks}>
          <a href="/tv-shows" className={styles.navLink}>
            TV Shows
          </a>
          <a href="/movies" className={styles.navLink}>
            Movies
          </a>
          <a href="/leave-review" className={styles.navLink}>
            Leave Review
          </a>
          <a href="/order-review" className={styles.navLink}>
            Order Review
          </a>
          <div className={styles.divider} />
          <button className={styles.signInBtn}>Sign In</button>
          <button className={styles.signUpBtn}>Sign Up</button>
        </div>
        <button className={styles.menuBtn} aria-label="Toggle menu">
          ☰
        </button>
      </div>
    </nav>
  );
}

export default Navigation;
