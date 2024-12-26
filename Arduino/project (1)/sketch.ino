#include <TM1637.h>

// Definicje pinów CLK i DIO dla TM1637
#define CLK 2
#define DIO 3

// Definicje pinów przycisków
#define BTN_INCREASE 4
#define BTN_DECREASE 5
#define BTN_SET_MINUTES 6
#define BTN_SET_SECONDS 7
#define BTN_START 11

// Utworzenie obiektu TM1637
TM1637 tm(CLK, DIO);

// Czas minutnika (w minutach i sekundach)
int countdownMinutes = 1;
int countdownSeconds = 0;

// Zmienna czasu do odliczania
unsigned long previousMillis = 0;
const long interval = 1000;  // Interwał 1 sekundy

// Flagi i stany
bool timerRunning = false;   // Flaga, czy minutnik jest włączony
bool editingMinutes = true;  // Flaga, czy edytujemy minuty (true) czy sekundy (false)

void setup() {
  // Ustawienie pinów przycisków jako wejścia
  pinMode(BTN_INCREASE, INPUT_PULLUP);
  pinMode(BTN_DECREASE, INPUT_PULLUP);
  pinMode(BTN_SET_MINUTES, INPUT_PULLUP);
  pinMode(BTN_SET_SECONDS, INPUT_PULLUP);
  pinMode(BTN_START, INPUT_PULLUP);

  // Ustawienie pinów dla buzzera i LED
  pinMode(8, OUTPUT);  // Ustawienie pinu 8 jako wyjścia dla buzzera
  pinMode(9, OUTPUT);  // Ustawienie pinu 9 jako wyjścia dla diody LED

  // Inicjalizacja wyświetlacza TM1637
  tm.init();
  tm.set(BRIGHT_TYPICAL);  // Ustawienie jasności wyświetlacza
  tm.point(true);          // Włączenie kropki dwukropka na wyświetlaczu

  // Wyświetlenie początkowego czasu
  displayTime();
}

void loop() {
  handleButtons();  // Obsługa przycisków

  // Uruchom minutnik tylko, gdy timer jest aktywny
  if (timerRunning) {
    timer();
    
    // Sprawdzenie, czy czas się skończył
    if (countdownMinutes == 0 && countdownSeconds == 0) {
      timerRunning = false;  // Zatrzymanie minutnika
      alarm();               // Uruchomienie alarmu
      delay(10000);          // Przerwa 10 sekund przed restartem
      countdownMinutes = 1;  // Reset minutnika na 1 minutę
      countdownSeconds = 0;
      displayTime();
    }
  }
}

void timer() {
  unsigned long currentMillis = millis();

  // Sprawdzenie, czy 1 sekunda minęła
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    // Odliczanie czasu
    if (countdownSeconds == 0) {
      if (countdownMinutes > 0) {
        countdownMinutes--;
        countdownSeconds = 59;
      }
    } else {
      countdownSeconds--;
    }

    // Wyświetlenie zaktualizowanego czasu na wyświetlaczu TM1637
    displayTime();
  }
}

void alarm() {
  for (int i = 0; i < 10; i++) {
    digitalWrite(9, HIGH);  // Włączenie diody LED
    tone(8, 262);           // Uruchomienie buzzera o częstotliwości 262 Hz
    delay(500);             // Opóźnienie 0.5 sekundy
    digitalWrite(9, LOW);   // Wyłączenie diody LED
    noTone(8);              // Wyłączenie buzzera
    delay(500);             // Opóźnienie 0.5 sekundy
  }
  digitalWrite(9, LOW);     // Upewnienie się, że LED jest wyłączona
  noTone(8);                // Upewnienie się, że buzzer jest wyłączony
}

void displayTime() {
  // Rozdzielenie minut i sekund na poszczególne cyfry
  int minutesTens = countdownMinutes / 10;
  int minutesUnits = countdownMinutes % 10;
  int secondsTens = countdownSeconds / 10;
  int secondsUnits = countdownSeconds % 10;

  // Wyświetlenie czasu w formacie MM:SS
  tm.display(0, minutesTens);    // Dziesiątki minut
  tm.display(1, minutesUnits);   // Jedności minut
  tm.display(2, secondsTens);    // Dziesiątki sekund
  tm.display(3, secondsUnits);   // Jedności sekund
}

void handleButtons() {
  // Zwiększanie minut lub sekund
  if (digitalRead(BTN_INCREASE) == LOW) {
    if (editingMinutes) {
      countdownMinutes = (countdownMinutes + 1) % 100;  // Maksymalnie 99 minut
    } else {
      countdownSeconds = (countdownSeconds + 1) % 60;   // Maksymalnie 59 sekund
    }
    displayTime();
    delay(200);  // Krótkie opóźnienie dla uniknięcia drgania styków
  }

  // Zmniejszanie minut lub sekund
  if (digitalRead(BTN_DECREASE) == LOW) {
    if (editingMinutes) {
      countdownMinutes = (countdownMinutes > 0) ? countdownMinutes - 1 : 0;
    } else {
      countdownSeconds = (countdownSeconds > 0) ? countdownSeconds - 1 : 0;
    }
    displayTime();
    delay(200);  // Krótkie opóźnienie dla uniknięcia drgania styków
  }

  // Ustawienie edytowania minut
  if (digitalRead(BTN_SET_MINUTES) == LOW) {
    editingMinutes = true;
    delay(200);  // Krótkie opóźnienie dla uniknięcia drgania styków
  }

  // Ustawienie edytowania sekund
  if (digitalRead(BTN_SET_SECONDS) == LOW) {
    editingMinutes = false;
    delay(200);  // Krótkie opóźnienie dla uniknięcia drgania styków
  }

  // Uruchamianie minutnika
  if (digitalRead(BTN_START) == LOW) {
    timerRunning = true;
    delay(200);  // Krótkie opóźnienie dla uniknięcia drgania styków
  }
}
