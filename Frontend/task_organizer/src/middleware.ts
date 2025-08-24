// middleware.ts
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

const loginRoute = "/";

export async function middleware(request: NextRequest) {
  const bearerToken = request.cookies.get("access_token");
  const authToken = request.cookies.get("authjs.session-token");
  const cookies = request.cookies;
  console.log("Cookies:", cookies);
  let Token = null;
  if (bearerToken){
    Token = bearerToken;
  }else if (authToken) {
    Token = authToken;
  }
//  if (authToken){
//   return NextResponse.next();
//  }
  // console.log("Cookies:", cookies);
  if (!Token) {
    return NextResponse.redirect(new URL(loginRoute, request.url));
  }

  try {
    console.log("Validating token via cookie...");
    const response = await fetch(`http://back01:8000/api/auth/mw`, {
      method: "GET",
      headers: {
      // Enviar el token como una cookie en el encabezado 'Cookie'
      'Cookie': `${Token.name}=${Token.value}`,
      },
    });

    // 3. Si la respuesta del backend es exitosa (200 OK)
    if (response.ok) {
      // Tomar la cookie de la respuesta del backend
      const newCookie = response.headers.get('Set-Cookie');

      // // La solicitud a la página protegida puede continuar.
      const res = NextResponse.next();

      // // 4. Reescribir la cookie en la respuesta al navegador
      if (newCookie) {
        res.headers.set('Set-Cookie', newCookie);
      }

      return res;
    }

    // 5. Si la respuesta no es 200 (ej. 401 Unauthorized)
    else {
      // Redirigir al login y borrar la cookie inválida
      const res = NextResponse.redirect(new URL(loginRoute, request.url));
      res.cookies.delete("access_token");
      return res;
    }
  } catch (error) {
    console.error("Error en el middleware de autenticación:", error);
    // En caso de error de red, redirigir al login por seguridad
    const res = NextResponse.redirect(new URL(loginRoute, request.url));
    res.cookies.delete("access_token");
    return res;
  }
}

// Configuración para el middleware.
export const config = {
  // Aquí puedes usar un matcher para que el middleware solo se ejecute en ciertas rutas
  matcher: [
    "/dashboard/:path*",
    "/projects/:path*",
    "/main/:path*",
    "/settings/:path*",
  ],
};
