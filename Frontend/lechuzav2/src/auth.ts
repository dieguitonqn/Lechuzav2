import NextAuth from "next-auth"
import Credentials from "next-auth/providers/credentials"
import Google from "next-auth/providers/google"
 

interface DataAuth {
  access_token: string
  refresh_token: string
  token_type: string
  user: {
    id: number
    name: string
    email: string
    role: string
  }
}

export const { handlers, signIn, signOut, auth } = NextAuth({
  providers: [
    Credentials({

      name: "Credentials",
      credentials: {

        email: { label: "Usuario", type: "text" },
        password: { label: "Contraseña", type: "password" }

      },
      async authorize(credentials) {
        console.log("🚀 Configurando proveedor de autenticación con credenciales") // Debug log

        const res = await fetch(`${process.env.AUTH_LOGIN_URL}`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            email: credentials?.email,
            password: credentials?.password
          })
        })

        const data:DataAuth = await res.json()
        console.log(`User response: ${JSON.stringify(data)}`)
        if (res.ok && data) {
          return data
        }

        return null
      }
    }),
    Google
  ],
  pages: {
    signIn: "/auth/signin"
  },
  callbacks:{
    async jwt({ token, user }) {
      // 1. Verificación de seguridad: solo entramos si 'user' existe (primer login)
      if (user) {
        // Ahora TypeScript NO marcará error aquí
        token.accessToken = user.access_token 
        token.refreshToken = user.refresh_token
        token.role = user.user.role
      }
      return token
    },
    async session({session,token}){
      if(token){    
        session.accessToken = token.accessToken as string
        session.refreshToken = token.refreshToken as string
        session.user.role = token.role as string

      }
      return session
      
    },
    async redirect({ url, baseUrl }) {
      
        return `${baseUrl}/main`
      
      
    }
  }
})