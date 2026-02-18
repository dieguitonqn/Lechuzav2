// next-auth.d.ts
import NextAuth, { DefaultSession } from "next-auth"

declare module "next-auth" {
  /**
   * Lo que devuelve tu función 'authorize' 
   * (Lo que viene de FastAPI)
   */
  interface User {
    access_token: string
    refresh_token: string
    user: {
      id: number
      name: string
      email: string
      role: string
    }
  }

  /**
   * Lo que ves cuando usas 'useSession' o 'auth()'
   */
  interface Session {
    accessToken: string
    refreshToken: string
    user: {
      id: number
      name: string
      email: string
      role: string
    } & DefaultSession["user"]
  }
}

declare module "next-auth/jwt" {
  /**
   * Lo que se guarda dentro de la cookie cifrada
   */
  interface JWT {
    accessToken: string
    refreshToken: string
    role: string
    userId: number
    userName: string
    userEmail: string
  }
}