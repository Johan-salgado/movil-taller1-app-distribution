# Taller 1 - Distribución de APK con Firebase App Distribution

**Asignatura:** Programación Móvil  
**Estudiante:** Johan Eliu Salgado Castro  
**Institución:** UCEVA  
**Repositorio:** https://github.com/Johan-salgado/movil-taller1-app-distribution.git  

---

## Descripción del Proyecto

Aplicación móvil desarrollada en Flutter diseñada para demostrar el flujo de distribución continua de versiones mediante **Firebase App Distribution**. Permite la distribución controlada a grupos de pruebas (QA) y la verificación del proceso de actualización en dispositivos Android reales.

---

## Flujo de Trabajo

El flujo implementado sigue el ciclo estándar de distribución móvil:

```
Generar APK (Release) ➔ Subir a Firebase App Distribution ➔ Notificar a Testers (QA_Clase) ➔ Instalación en Dispositivo ➔ Actualización Incremental
```

1. **Generación del APK**: Compilación en modo release (`flutter build apk`).
2. **App Distribution**: Carga del binario en la consola de Firebase con sus respectivas Release Notes.
3. **Testers**: Distribución automática al grupo de pruebas `QA_Clase` (incluyendo `dduran@uceva.edu.co`).
4. **Instalación**: El tester recibe la invitación por correo electrónico o mediante enlace directo y descarga la aplicación.
5. **Actualización**: Se publica una nueva versión con cambios visibles e incremento en `versionCode`/`versionName`, permitiendo actualizar sobre la versión previa.

---

## Publicación (Paso a Paso para Replicar)

### 1. Compilación Release
```bash
flutter build apk
```
El archivo generado se ubicará en:
`build/app/outputs/flutter-apk/app-release.apk`

### 2. Configuración en Firebase Console
1. Acceder a [Firebase Console](https://console.firebase.google.com/) y abrir/crear el proyecto del taller.
2. Registrar la aplicación Android utilizando el `applicationId` configurado en `android/app/build.gradle.kts`:
   - `com.johansalgado.taller_app_distribution`
3. Navegar a **Release & Monitor > App Distribution**.
4. En la pestaña **Testers y grupos**:
   - Crear el grupo: `QA_Clase`.
   - Agregar el correo del evaluador/tester: `dduran@uceva.edu.co`.

### 3. Distribución del Release
1. En la pestaña **Releases**, arrastrar el archivo `app-release.apk`.
2. Asignar el release al grupo `QA_Clase`.
3. Redactar las **Release Notes** descriptivas.
4. Clic en **Distribuir** y copiar el enlace de invitación o descarga.

---

## Notas sobre Versionado

El versionado se maneja en el archivo `pubspec.yaml` siguiendo la convención de Flutter `version: <versionName>+<versionCode>`:

- **Versión Inicial:** `1.0.0+1`
  - `versionName`: `1.0.0`
  - `versionCode`: `1`
- **Versión Incremental (Actualización):** `1.0.1+2`
  - `versionName`: `1.0.1`
  - `versionCode`: `2`

### Formato de Release Notes Usado
```text
[vX.Y.Z] - YYYY-MM-DD
Responsable: Johan Eliu Salgado Castro
Cambios:
- Descripción puntual del cambio 1
- Descripción puntual del cambio 2
```

---

## Capturas y Evidencias

*(Espacio reservado para enlaces de capturas y GIFs del panel de Firebase App Distribution y funcionamiento en el dispositivo)*

| Evidencia | Descripción |
|-----------|-------------|
| Panel de Releases | Vista general de las versiones 1.0.0 y 1.0.1 publicadas |
| Grupo de Testers | Registro de `dduran@uceva.edu.co` en `QA_Clase` |
| Correo de Invitación | Recepción del correo de Firebase App Distribution |
| App Instalada v1.0.0 | Captura en dispositivo físico de la versión inicial |
| Actualización a v1.0.1 | Captura en dispositivo físico de la actualización |
