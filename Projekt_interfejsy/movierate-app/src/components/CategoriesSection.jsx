import React from 'react'

const CategoriesSection = () => {
  const categories = [
    { name: 'Action', count: 'Finding adventure' },
    { name: 'Drama', count: 'Emotional stories' },
    { name: 'Comedy', count: 'Laugh out loud' },
    { name: 'Sci-Fi', count: 'Future worlds' }
  ]

  return (
    <section className="categories-section">
      <h2 className="section-title">Categories</h2>
      
      <div className="categories-grid">
        {categories.map((category, index) => (
          <div key={index} className="category-item">
            <h3 className="category-name">{category.name}</h3>
            <p className="category-description">{category.count}</p>
          </div>
        ))}
      </div>
    </section>
  )
}

export default CategoriesSection