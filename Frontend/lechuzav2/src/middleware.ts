// middleware.ts
import { auth } from "@/auth";
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

const loginRoute = "/auth/signin";
const publicRoutes = ["/", "/login", "/register"];
const adminRoutes = ["/settings", "/admin"];

export async function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;
  
  console.log("🚀 Middleware ejecutándose para:", pathname); // Debug log
  
  // Verificar si es una ruta pública
  const isPublicRoute = publicRoutes.some(
    (route) => pathname === route
  );
  
  console.log("📍 Es ruta pública?:", isPublicRoute); // Debug log
  
  // Obtener la sesión
  const session = await auth();
  console.log("👤 Sesión encontrada?:", !!session); // Debug log

  if (session && isPublicRoute && pathname.startsWith(loginRoute)) {
    console.log("🔄 Redirigiendo a /main - Usuario autenticado en ruta pública");
    return NextResponse.redirect(new URL("/main", request.url));
  }
  
  // Si no hay sesión y no es una ruta pública
  if (!session && !isPublicRoute) {
    console.log("🔒 Bloqueando acceso - Sin sesión"); // Debug log
    const loginUrl = new URL(loginRoute, request.url);
    loginUrl.searchParams.set("callbackUrl", request.url);
    return NextResponse.redirect(loginUrl);
  }
  
  // Verificar rutas de administrador
  // const isAdminRoute = adminRoutes.some(
  //   (route) => pathname.startsWith(route)
  // );
  
  // if (isAdminRoute && session) {
  //   const isAdmin = session.user?.role === "admin";
    
  //   if (!isAdmin) {
  //     return NextResponse.redirect(new URL("/main", request.url));
  //   }
  // }
  
  // // Si hay sesión y está en la página de login, redirigir al dashboard
  // if (session && pathname === loginRoute) {
  //   return NextResponse.redirect(new URL("/main", request.url));
  // }
  
  console.log("✅ Permitiendo acceso"); // Debug log
  return NextResponse.next();
}

export const config = {
  matcher: [
    "/dashboard/:path*",
    "/projects/:path*",
    "/main/:path*", 
    "/settings/:path*",
    "/",
  ],
};
