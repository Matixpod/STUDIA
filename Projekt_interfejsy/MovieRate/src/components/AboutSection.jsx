import React from "react";
import styles from "./styles/AboutSection.module.css";

function AboutSection() {
  return (
    <section className={styles.aboutSection}>
      <div className={styles.aboutContent}>
        <h2 className={styles.aboutTitle}>About Us</h2>
        <p className={styles.aboutText}>
          We're passionate about bringing you the best movie and series reviews.
          Our platform helps you discover amazing content and share your
          thoughts with a community of fellow entertainment enthusiasts.
        </p>
      </div>
    </section>
  );
}

export default AboutSection;
