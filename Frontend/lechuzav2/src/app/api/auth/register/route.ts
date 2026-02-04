import { NextRequest, NextResponse } from "next/server";
import bcrypt from "bcryptjs";

interface RegisterRequest {
    firstName: string;
    lastName: string;
    email: string;
    password: string;
    turnstileToken: string;
}

async function verifyTurnstile(token: string, ip?: string) {
    const secretKey = process.env.TURNSTILE_SECRET_KEY;
    
    if (!secretKey) {
        throw new Error("Turnstile secret key not configured");
    }

    const formData = new FormData();
    formData.append('secret', secretKey);
    formData.append('response', token);
    if (ip) {
        formData.append('remoteip', ip);
    }

    const response = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
        method: 'POST',
        body: formData,
    });

    const result = await response.json();
    return result.success;
}

export async function POST(request: NextRequest) {
    try {
        const body: RegisterRequest = await request.json();
        const { firstName, lastName, email, password, turnstileToken } = body;

        // Validate required fields
        if (!firstName || !lastName || !email || !password || !turnstileToken) {
            return NextResponse.json(
                { message: "Todos los campos son obligatorios" },
                { status: 400 }
            );
        }

        // Get client IP for Turnstile verification
        const clientIP = request.headers.get('x-forwarded-for') || 
                        request.headers.get('x-real-ip') || 
                        'unknown';

        // Verify Turnstile token
        const turnstileValid = await verifyTurnstile(turnstileToken, clientIP);
        
        if (!turnstileValid) {
            return NextResponse.json(
                { message: "Verificación de seguridad fallida" },
                { status: 400 }
            );
        }

        // Basic email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            return NextResponse.json(
                { message: "Formato de email inválido" },
                { status: 400 }
            );
        }

        // Password validation
        if (password.length < 8) {
            return NextResponse.json(
                { message: "La contraseña debe tener al menos 8 caracteres" },
                { status: 400 }
            );
        }

        // Here you would typically:
        // 1. Hash the password
        // 2. Check if email already exists
        // 3. Save user to database
        // 4. Send verification email (optional)
        
        // For now, we'll just simulate success
        // TODO: Implement actual user creation logic
        
        // Simulate checking if user already exists
        // In a real app, you'd check your database
        if (email === "test@example.com") {
            return NextResponse.json(
                { message: "Ya existe una cuenta con este email" },
                { status: 400 }
            );
        }

        // Hash password
        const hashedPassword = await bcrypt.hash(password, 12);

        // Save user to database
        // const user = await createUser({
        //     firstName,
        //     lastName,
        //     email,
        //     password: hashedPassword,
        // });

        console.log("New user registration attempt:", { firstName, lastName, email });

        return NextResponse.json(
            { 
                message: "Cuenta creada exitosamente",
                user: { firstName, lastName, email } 
            },
            { status: 201 }
        );

    } catch (error) {
        console.error("Registration error:", error);
        return NextResponse.json(
            { message: "Error interno del servidor" },
            { status: 500 }
        );
    }
}