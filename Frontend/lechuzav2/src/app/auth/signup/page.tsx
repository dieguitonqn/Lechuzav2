"use client";

import { useState, useRef } from "react";
import { useRouter } from "next/navigation";
import Image from "next/image";
import { Turnstile } from "@marsidev/react-turnstile";

export default function SignUp() {
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState("");
    const [success, setSuccess] = useState("");
    const [turnstileToken, setTurnstileToken] = useState("");
    const turnstileRef = useRef(null);
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setIsLoading(true);
        setError("");
        setSuccess("");

        if (!turnstileToken) {
            setError("Por favor, completa la verificación de seguridad");
            setIsLoading(false);
            return;
        }

        const formData = new FormData(e.currentTarget);
        const firstName = formData.get("firstName") as string;
        const lastName = formData.get("lastName") as string;
        const email = formData.get("email") as string;
        const password = formData.get("password") as string;
        const confirmPassword = formData.get("confirmPassword") as string;

        if (password !== confirmPassword) {
            setError("Las contraseñas no coinciden");
            setIsLoading(false);
            return;
        }

        try {
            const response = await fetch("/api/auth/register", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    firstName,
                    lastName,
                    email,
                    password,
                    turnstileToken,
                }),
            });

            if (response.ok) {
                setSuccess("Cuenta creada exitosamente. Redirigiendo al inicio de sesión...");
                setTimeout(() => {
                    router.push("/auth/signin");
                }, 2000);
            } else {
                const data = await response.json();
                setError(data.message || "Error al crear la cuenta");
            }
        } catch (error) {
            setError("Error de conexión. Intenta nuevamente.");
        } finally {
            setIsLoading(false);
        }
    };

    const handleTurnstileSuccess = (token: string) => {
        setTurnstileToken(token);
        setError("");
    };

    const handleTurnstileError = () => {
        setTurnstileToken("");
        setError("Error en la verificación de seguridad. Intenta nuevamente.");
    };

    return (
        <div className="h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 flex flex-col">
            <div className="flex-1 flex">
                {/* Video Section */}
                <div className="flex-[3] relative overflow-hidden hidden md:block">
                    {/* Video Background */}
                    <video
                        className="absolute inset-0 w-full h-full object-cover"
                        autoPlay
                        loop
                        muted
                        playsInline
                    >
                        <source src="/videos/background-video.mp4" type="video/mp4" />
                    </video>

                    {/* Gradient Overlay */}
                    <div className="absolute inset-0 bg-gradient-to-r from-slate-900/80 via-slate-800/50 to-transparent"></div>

                    {/* Content Overlay */}
                    <div className="relative z-10 h-full flex flex-col justify-center px-12">
                        <div className="max-w-lg">
                            <h1 className="text-6xl font-bold text-white mb-6 leading-tight">
                                Únete a
                                <span className="block text-blue-400">Lechuza</span>
                            </h1>
                            <p className="text-xl text-slate-300 leading-relaxed">
                                Crea tu cuenta y accede a todas las funcionalidades de nuestra plataforma.
                                Una experiencia única te espera.
                            </p>
                        </div>
                    </div>
                </div>

                {/* Form Section */}
                <div className="flex-[2] flex items-center justify-center p-8 bg-slate-900/95 backdrop-blur-sm">
                    <div className="w-full max-w-md">
                        {/* Logo */}
                        <div className="text-center mb-8">
                            <div className="inline-flex items-center justify-center w-16 h-16 bg-blue-600 rounded-2xl mb-4">
                                <Image
                                    src="/logo.svg"
                                    alt="Lechuza Logo"
                                    width={32}
                                    height={32}
                                    className="text-white"
                                />
                            </div>
                            <h2 className="text-3xl font-bold text-white">Crear Cuenta</h2>
                            <p className="text-slate-400 mt-2">Completa tus datos para registrarte</p>
                        </div>

                        {/* Error/Success Messages */}
                        {error && (
                            <div className="bg-red-500/10 border border-red-500/20 rounded-lg p-4 mb-6">
                                <p className="text-red-400 text-sm">{error}</p>
                            </div>
                        )}

                        {success && (
                            <div className="bg-green-500/10 border border-green-500/20 rounded-lg p-4 mb-6">
                                <p className="text-green-400 text-sm">{success}</p>
                            </div>
                        )}

                        {/* Registration Form */}
                        <form onSubmit={handleSubmit} className="space-y-6">
                            {/* Name Fields */}
                            <div className="grid grid-cols-2 gap-4">
                                <div>
                                    <label htmlFor="firstName" className="block text-sm font-medium text-slate-300 mb-2">
                                        Nombre
                                    </label>
                                    <input
                                        id="firstName"
                                        name="firstName"
                                        type="text"
                                        required
                                        className="w-full px-4 py-3 bg-slate-800/50 border border-slate-700 rounded-lg text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                                        placeholder="Tu nombre"
                                    />
                                </div>
                                <div>
                                    <label htmlFor="lastName" className="block text-sm font-medium text-slate-300 mb-2">
                                        Apellido
                                    </label>
                                    <input
                                        id="lastName"
                                        name="lastName"
                                        type="text"
                                        required
                                        className="w-full px-4 py-3 bg-slate-800/50 border border-slate-700 rounded-lg text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                                        placeholder="Tu apellido"
                                    />
                                </div>
                            </div>

                            {/* Email Field */}
                            <div>
                                <label htmlFor="email" className="block text-sm font-medium text-slate-300 mb-2">
                                    Correo Electrónico
                                </label>
                                <input
                                    id="email"
                                    name="email"
                                    type="email"
                                    autoComplete="email"
                                    required
                                    className="w-full px-4 py-3 bg-slate-800/50 border border-slate-700 rounded-lg text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                                    placeholder="tu@email.com"
                                />
                            </div>

                            {/* Password Fields */}
                            <div>
                                <label htmlFor="password" className="block text-sm font-medium text-slate-300 mb-2">
                                    Contraseña
                                </label>
                                <input
                                    id="password"
                                    name="password"
                                    type="password"
                                    autoComplete="new-password"
                                    required
                                    minLength={8}
                                    className="w-full px-4 py-3 bg-slate-800/50 border border-slate-700 rounded-lg text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                                    placeholder="Mínimo 8 caracteres"
                                />
                            </div>

                            <div>
                                <label htmlFor="confirmPassword" className="block text-sm font-medium text-slate-300 mb-2">
                                    Confirmar Contraseña
                                </label>
                                <input
                                    id="confirmPassword"
                                    name="confirmPassword"
                                    type="password"
                                    autoComplete="new-password"
                                    required
                                    minLength={8}
                                    className="w-full px-4 py-3 bg-slate-800/50 border border-slate-700 rounded-lg text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                                    placeholder="Repite tu contraseña"
                                />
                            </div>

                            {/* Cloudflare Turnstile */}
                            <div className="flex justify-center">
                                <Turnstile
                                    ref={turnstileRef}
                                    siteKey={process.env.NEXT_PUBLIC_TURNSTILE_SITE_KEY || "0x4AAAAAAABkMYinukE_q4yV"}
                                    onSuccess={handleTurnstileSuccess}
                                    onError={handleTurnstileError}
                                />
                            </div>

                            {/* Submit Button */}
                            <button
                                type="submit"
                                disabled={isLoading || !turnstileToken}
                                className="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-slate-700 disabled:cursor-not-allowed text-white font-semibold py-3 px-4 rounded-lg transition-all duration-200 transform hover:scale-[1.02] active:scale-[0.98]"
                            >
                                {isLoading ? (
                                    <div className="flex items-center justify-center">
                                        <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
                                        Creando cuenta...
                                    </div>
                                ) : (
                                    "Crear Cuenta"
                                )}
                            </button>

                            {/* Sign In Link */}
                            <div className="text-center">
                                <p className="text-slate-400">
                                    ¿Ya tienes cuenta?{" "}
                                    <button
                                        type="button"
                                        onClick={() => router.push("/auth/signin")}
                                        className="text-blue-400 hover:text-blue-300 font-medium transition-colors duration-200"
                                    >
                                        Inicia sesión aquí
                                    </button>
                                </p>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    );
}
