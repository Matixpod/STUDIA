import React, { useState } from 'react'
import { Settings as SettingsIcon, X, Moon, Sun, Type, Eye, Palette, ChevronDown } from 'lucide-react'
import { useSettings } from '../context/SettingsContext'

const Settings = () => {
  const [isOpen, setIsOpen] = useState(false)
  const { settings, updateSetting } = useSettings()

  return (
    <>
      {/* Przycisk ustawień */}
      <button 
        className="settings-button"
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Otwórz ustawienia dostępności"
      >
        <SettingsIcon size={20} />
      </button>

      {/* Panel ustawień */}
      {isOpen && (
        <>
          <div className="settings-overlay" onClick={() => setIsOpen(false)} />
          <div className="settings-panel">
            <div className="settings-header">
              <h2>Ustawienia dostępności</h2>
              <button 
                className="settings-close"
                onClick={() => setIsOpen(false)}
                aria-label="Zamknij ustawienia"
              >
                <X size={24} />
              </button>
            </div>

            <div className="settings-content">
              {/* Tryb ciemny */}
              <div className="setting-item">
                <div className="setting-info">
                  {settings.darkMode ? <Moon size={20} /> : <Sun size={20} />}
                  <div>
                    <h3>Tryb ciemny</h3>
                    <p>Zmniejsz jasność interfejsu</p>
                  </div>
                </div>
                <label className="toggle-switch">
                  <input
                    type="checkbox"
                    checked={settings.darkMode}
                    onChange={(e) => updateSetting('darkMode', e.target.checked)}
                  />
                  <span className="toggle-slider"></span>
                </label>
              </div>

              {/* Rozmiar czcionki */}
              <div className="setting-item">
                <div className="setting-info">
                  <Type size={20} />
                  <div>
                    <h3>Rozmiar tekstu</h3>
                    <p>Dostosuj wielkość czcionki</p>
                  </div>
                </div>
                <select 
                  value={settings.fontSize} 
                  onChange={(e) => updateSetting('fontSize', e.target.value)}
                  className="setting-select"
                >
                  <option value="small">Mały</option>
                  <option value="normal">Normalny</option>
                  <option value="large">Duży</option>
                  <option value="xlarge">Bardzo duży</option>
                </select>
              </div>

              {/* Wysoki kontrast */}
              <div className="setting-item">
                <div className="setting-info">
                  <Eye size={20} />
                  <div>
                    <h3>Wysoki kontrast</h3>
                    <p>Zwiększ kontrast kolorów</p>
                  </div>
                </div>
                <label className="toggle-switch">
                  <input
                    type="checkbox"
                    checked={settings.highContrast}
                    onChange={(e) => updateSetting('highContrast', e.target.checked)}
                  />
                  <span className="toggle-slider"></span>
                </label>
              </div>

              {/* Redukcja animacji */}
              <div className="setting-item">
                <div className="setting-info">
                  <ChevronDown size={20} />
                  <div>
                    <h3>Ogranicz animacje</h3>
                    <p>Wyłącz efekty przejścia</p>
                  </div>
                </div>
                <label className="toggle-switch">
                  <input
                    type="checkbox"
                    checked={settings.reduceMotion}
                    onChange={(e) => updateSetting('reduceMotion', e.target.checked)}
                  />
                  <span className="toggle-slider"></span>
                </label>
              </div>

              {/* Tryb dla daltonistów */}
              <div className="setting-item">
                <div className="setting-info">
                  <Palette size={20} />
                  <div>
                    <h3>Filtr kolorów</h3>
                    <p>Dla osób z zaburzeniami widzenia barw</p>
                  </div>
                </div>
                <select 
                  value={settings.colorBlindMode} 
                  onChange={(e) => updateSetting('colorBlindMode', e.target.value)}
                  className="setting-select"
                >
                  <option value="none">Wyłączony</option>
                  <option value="protanopia">Protanopia</option>
                  <option value="deuteranopia">Deuteranopia</option>
                  <option value="tritanopia">Tritanopia</option>
                </select>
              </div>
            </div>

            <div className="settings-footer">
              <button 
                className="reset-button"
                onClick={() => {
                  updateSetting('darkMode', false)
                  updateSetting('fontSize', 'normal')
                  updateSetting('highContrast', false)
                  updateSetting('reduceMotion', false)
                  updateSetting('colorBlindMode', 'none')
                }}
              >
                Przywróć domyślne
              </button>
            </div>
          </div>
        </>
      )}
    </>
  )
}

export default Settings