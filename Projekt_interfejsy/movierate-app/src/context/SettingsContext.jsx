import React, { createContext, useContext, useState, useEffect } from 'react'

const SettingsContext = createContext()

export const useSettings = () => {
  const context = useContext(SettingsContext)
  if (!context) {
    throw new Error('useSettings must be used within SettingsProvider')
  }
  return context
}

export const SettingsProvider = ({ children }) => {
  const [settings, setSettings] = useState(() => {
    const saved = localStorage.getItem('movierate-settings')
    return saved ? JSON.parse(saved) : {
      darkMode: false,
      fontSize: 'normal', // small, normal, large, xlarge
      highContrast: false,
      reduceMotion: false,
      colorBlindMode: 'none' // none, protanopia, deuteranopia, tritanopia
    }
  })

  useEffect(() => {
    localStorage.setItem('movierate-settings', JSON.stringify(settings))
    
    // Aplikuj ustawienia do dokumentu
    const root = document.documentElement
    
    // Dark mode
    if (settings.darkMode) {
      root.classList.add('dark-mode')
    } else {
      root.classList.remove('dark-mode')
    }
    
    // Font size
    root.setAttribute('data-font-size', settings.fontSize)
    
    // High contrast
    if (settings.highContrast) {
      root.classList.add('high-contrast')
    } else {
      root.classList.remove('high-contrast')
    }
    
    // Reduce motion
    if (settings.reduceMotion) {
      root.classList.add('reduce-motion')
    } else {
      root.classList.remove('reduce-motion')
    }
    
    // Color blind mode
    root.setAttribute('data-color-blind-mode', settings.colorBlindMode)
    
  }, [settings])

  const updateSetting = (key, value) => {
    setSettings(prev => ({ ...prev, [key]: value }))
  }

  return (
    <SettingsContext.Provider value={{ settings, updateSetting }}>
      {children}
    </SettingsContext.Provider>
  )
}