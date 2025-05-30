import React, { createContext, useContext } from 'react'
import useOrders from '../hooks/useOrders'

const OrdersContext = createContext()

export const useOrdersContext = () => {
  const context = useContext(OrdersContext)
  if (!context) {
    throw new Error('useOrdersContext must be used within OrdersProvider')
  }
  return context
}

export const OrdersProvider = ({ children }) => {
  const ordersData = useOrders()

  return (
    <OrdersContext.Provider value={ordersData}>
      {children}
    </OrdersContext.Provider>
  )
}