"use client";

import { signIn } from "next-auth/react";
import { useState } from "react";
import { useRouter } from "next/navigation";
import Image from "next/image";
import Link from "next/link";

export default function SignIn() {
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState("");
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setIsLoading(true);
        setError("");

        const formData = new FormData(e.currentTarget);
        const email = formData.get("email") as string;
        const password = formData.get("password") as string;

        try {
            const result = await signIn("credentials", {
                email,
                password,
                redirect: false,
            });

            if (result?.error) {
                setError("Credenciales inválidas");
            } else {
                router.push("/main");
            }
        } catch (error) {
            setError("Error al iniciar sesión");
        } finally {
            setIsLoading(false);
        }
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
                        <source src="/lechuza.webm" type="video/webm" />
                        <div className="w-full h-full bg-gradient-to-br from-amber-100 to-amber-200 flex items-center justify-center">
                            <span className="text-6xl">🦉</span>
                        </div>
                    </video>

                    {/* Video Overlay */}
                    <div className="absolute inset-0 bg-gradient-to-r from-black/40 via-transparent to-black/20"></div>

                    {/* Overlay Content */}
                    <div className="absolute top-1 right-0 left-0 z-20 text-white">
                        <div className="max-w-7xl mx-auto">
                            <div className="flex justify-between items-center">
                                {/* Columna izquierda */}
                                <div className="flex flex-col">
                                    <Image 
                                    src={"/EPENLogo.png"}
                                    alt="EPEN Logo"
                                    width={300}
                                    height={300}
                                    className="mb-4 w-24 h-24 lg:w-36 lg:h-36 object-contain bg-slate-50/5 rounded-full p-2"
                                    />

                                </div>

                                {/* Columna derecha */}
                                
                                <div className="flex flex-col">
                                    <h1 className="text-2xl lg:text-4xl font-bold mb-1">Lechuza</h1>
                                    <p className="text-sm lg:text-lg text-gray-200">Sistema de Gestión Documental de Obras</p>
                                    <p className="mt-1 lg:mt-2 max-w-md text-gray-300 text-sm lg:text-base">EPEN - Ente Provincial de Energía de Neuquén</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                {/* Form Section */}
                <div className="flex-[1] flex items-center justify-center p-8 bg-white">
                    <div className="w-full max-w-md">
                        <div className="text-center mb-8">
                            <div className="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-amber-400 to-orange-500 rounded-2xl mb-4">
                                <span className="text-2xl">🦉</span>
                            </div>
                            <h2 className="text-2xl font-bold text-gray-900 mb-2">Inicio de sesión</h2>
                            <p className="text-gray-600">Accede a tu cuenta de Lechuza</p>
                        </div>

                        <form onSubmit={handleSubmit} className="space-y-6">
                            <div>
                                <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-2">
                                    Correo Electrónico
                                </label>
                                <input
                                    id="email"
                                    name="email"
                                    type="email"
                                    required
                                    className="w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                                    placeholder="usuario@epen.gov.ar"
                                />
                            </div>

                            <div>
                                <label htmlFor="password" className="block text-sm font-medium text-gray-700 mb-2">
                                    Contraseña
                                </label>
                                <input
                                    id="password"
                                    name="password"
                                    type="password"
                                    required
                                    className="w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
                                    placeholder="••••••••"
                                />
                            </div>

                            {error && (
                                <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-xl text-sm">
                                    {error}
                                </div>
                            )}

                            <button
                                type="submit"
                                disabled={isLoading}
                                className="w-full bg-gradient-to-r from-blue-600 to-purple-600 text-white py-3 px-4 rounded-xl font-medium hover:from-blue-700 hover:to-purple-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center"
                            >
                                {isLoading ? (

                                    <>
                                        <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
                                        Iniciando sesión...
                                    </>
                                ) : (
                                    "Iniciar Sesión"
                                )}
                            </button>
                        </form>

                        <div className="mt-6 text-center">
                            <p className="text-sm text-gray-600">
                                ¿No tenés usuario?{" "}
                                <Link href="/auth/signup" className="font-medium text-blue-600 hover:text-blue-500 transition-colors">
                                    ¡Regístrate!
                                </Link>
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            {/* Footer */}
            <footer className="flex flex-row  justify-center items-center bg-gradient-to-tr from-gray-900 to-slate-500 transition-discrete border-t border-gray-200 py-2 px-8 flex-shrink-0 gap-2">
                <div className="text-center text-sm text-gray-500">
                    Lechuza v1.0.0 - Sistema de Gestión Documental de Obras © 2024 EPEN

                </div>
                <a href="https://diarmodev.com"><Image src={"/diarmodev_logo5.webp"} alt="DiarmoDev Logo" width={30} height={30} /></a>
            </footer>
        </div>
    );
}