def angle(np, a, b):
  """
  Функция возвращает два значения.
  Первое - anglegrad - это угол между двумя векторами в градусах,
  Второе - anglerad - это угол между двумя векторами в радианах.
  """ 
  # Скалярное произведение двух векторов
  scalar = np.dot(a,b)
  # Нормирование первого и второго вектора
  norma = np.linalg.norm(a)
  normb = np.linalg.norm(b)
  # Получение угла между двумя векторами в радианах
  anglerad = np.arccos(norma/(norma*normb))
  # Перевод в градусы
  anglegrad = np.rad2deg(anglerad)
  return (anglegrad, anglerad)