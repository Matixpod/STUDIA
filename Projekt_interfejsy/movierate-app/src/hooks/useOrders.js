import { useState, useEffect } from 'react'

const useOrders = () => {
  const [orders, setOrders] = useState(() => {
    // Pobierz dane z localStorage przy inicjalizacji
    const savedOrders = localStorage.getItem('movierate-orders')
    return savedOrders ? JSON.parse(savedOrders) : []
  })

  // Zapisz do localStorage przy każdej zmianie
  useEffect(() => {
    localStorage.setItem('movierate-orders', JSON.stringify(orders))
  }, [orders])

  const addOrder = (newOrder) => {
    const order = {
      ...newOrder,
      id: Date.now(), // Prosty sposób generowania ID
      createdAt: new Date().toISOString(),
      currentReviewers: 0
    }
    setOrders(prev => [...prev, order])
    return order
  }

  const updateOrder = (orderId, updates) => {
    setOrders(prev => 
      prev.map(order => 
        order.id === orderId ? { ...order, ...updates } : order
      )
    )
  }

  const deleteOrder = (orderId) => {
    setOrders(prev => prev.filter(order => order.id !== orderId))
  }

  const applyToOrder = (orderId) => {
    setOrders(prev => 
      prev.map(order => 
        order.id === orderId 
          ? { ...order, currentReviewers: order.currentReviewers + 1 }
          : order
      )
    )
  }

  return {
    orders,
    addOrder,
    updateOrder,
    deleteOrder,
    applyToOrder
  }
}

export default useOrders