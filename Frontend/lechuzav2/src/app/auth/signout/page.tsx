'use client';

import React from "react";
import { logout } from "./actions";
import { useEffect } from "react";
import {signOut} from "next-auth/react";

export default function SignOut() {
  useEffect(() => {
    signOut();
  }, []);

    return (
    <div className="h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 flex items-center justify-center">
      <div className="text-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-white mx-auto mb-4"></div>
        <p className="text-white text-lg">Cerrando sesión...</p>
      </div>
    </div>
  );
}