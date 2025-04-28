import React from "react";
import styles from "./styles/CategoryCard.module.css";

function CategoryCard({ title, description }) {
  return (
    <article className={styles.categoryCard}>
      <h3 className={styles.categoryTitle}>{title}</h3>
      <p className={styles.categoryDescription}>{description}</p>
    </article>
  );
}

export default CategoryCard;
