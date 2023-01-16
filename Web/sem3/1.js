

const value = parseFloat(prompt('Введите температуру в цельсиях'));
alert(`Температура в цельсиях: ${value}, в градусах Фаренгейта это: ${(9 * value / 5 + 32).toFixed(1)}.`)