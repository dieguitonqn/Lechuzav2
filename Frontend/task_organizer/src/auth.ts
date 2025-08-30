import NextAuth from "next-auth"
import Credentials from "next-auth/providers/credentials"
import Google from "next-auth/providers/google"
 
export const { handlers, signIn, signOut, auth } = NextAuth({
  providers: [
    Credentials({
      name: "Credentials",
      credentials: {
        email: { label: "Email", type: "text" },
        password: { label: "Password", type: "password" }
      },
      async authorize(credentials) {
        const res = await fetch(`${process.env.AUTH_LOGIN_URL}`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            email: credentials?.email,
            password: credentials?.password
          })
        })

        const user = await res.json()
        console.log(`User response: ${JSON.stringify(user)}`)
        if (res.ok && user) {
          return user
        }

        return null
      }
    }),
    Google
  ],
  callbacks:{
    async redirect({ url, baseUrl }) {
      
        return `${baseUrl}/main`
      
      
    }
  }
})