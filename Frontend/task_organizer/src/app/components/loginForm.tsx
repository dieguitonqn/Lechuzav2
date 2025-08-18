"use client";
import { signIn } from "next-auth/react";
import React, { useState } from "react";

const LoginForm: React.FC = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [googleId, setGoogleId] = useState(null);
  const [loginOk, setLoginOk] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");

    try {
      const response = await fetch("/fapi/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include", // Include cookies in the request
        body: JSON.stringify({ email, password, googleId }),
      });

      if (!response.ok) {
        throw new Error("Login failed");
      }
      setLoginOk(true);

      window.location.href = "/main"; // Redirect to the main page after successful login
    } catch (err: unknown) {
      if (err instanceof Error) {
        // alert(err.message);
        setError(err.message);
      } else {
        alert("An unexpected error occurred");
      }
    }
  };

  return (
    <div className="max-w-md w-full p-6 bg-white rounded-lg shadow-md text-gray-800">
      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            className="w-full p-2 border border-gray-300 rounded"
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            className="w-full p-2 border border-gray-300 rounded"
          />
        </div>
        <div className="text-red-500 mt-2 text-center">
          {error && <p className="error">{error}</p>}
        </div>
        <div className="text-green-500 mt-2 text-center">
          {loginOk && <p className="success">Login Successful</p>}
        </div>
        <button
          type="submit"
          className="mt-4 w-full p-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          Login
        </button>
        <button
          type="button"
          className="mt-4 w-full p-2 bg-red-500 text-white rounded hover:bg-red-600"
          onClick={() => {
             signIn("google");
          }}
        >
          Login with Google
        </button>
      </form>
    </div>
  );
};

export default LoginForm;
