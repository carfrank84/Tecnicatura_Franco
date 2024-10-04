edad = int(input("Ingrese su edad para recibir un mensaje : "))


if 0 <= edad <= 9:
    print("La infancia es increíble y bella.")
elif 10 <= edad <= 19:
    print("Tienes muchos cambios, mucho que estudiar.")
elif 20 <= edad <= 29:
    print("Amor y confianza en el trabajo.")
elif 30 <= edad <= 39:
    print("Es una etapa de estabilidad y crecimiento personal.")
elif 40 <= edad <= 49:
    print("Consolidación profesional y personal.")
elif 50 <= edad <= 59:
    print("Tiempo de reflexión y disfrutar de los logros.")
elif 60 <= edad <= 69:
    print("Disfrutando de la madurez y sabiduría.")
elif 70 <= edad <= 79:
    print("Disfruta de tu tiempo y comparte tu experiencia.")
elif 80 <= edad <= 89:
    print("Etapa de paz y satisfacción con la vida.")
elif edad >= 90:
    print("Una vida llena de recuerdos valiosos.")
else:
    print("Edad no valida.")