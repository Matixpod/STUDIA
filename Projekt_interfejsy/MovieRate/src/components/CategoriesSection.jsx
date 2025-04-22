import React from "react";
import CategoryCard from "./CategoryCard";
import styles from "./styles/CategoriesSection.module.css";

function CategoriesSection() {
  const categories = [
    { title: "Action", description: "Thrilling adventures" },
    { title: "Drama", description: "Emotional stories" },
    { title: "Comedy", description: "Laugh out loud" },
    { title: "Sci-Fi", description: "Future worlds" },
  ];

  return (
    <section className={styles.categoriesSection}>
      <div className={styles.categoriesContent}>
        <h2 className={styles.sectionTitle}>Categories</h2>
        <div className={styles.categoriesGrid}>
          {categories.map((category, index) => (
            <CategoryCard
              key={index}
              title={category.title}
              description={category.description}
            />
          ))}
        </div>
      </div>
    </section>
  );
}

export default CategoriesSection;
