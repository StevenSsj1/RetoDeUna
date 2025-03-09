// src/pages/api/transactions/[userId].ts
import type { APIRoute } from "astro"

export const GET: APIRoute = async ({ params, request }) => {
  try {
    const userId = params.userId
    // Tomamos el query param "format"
    const url = new URL(request.url)

    // Llamamos a nuestro backend de FastAPI
    const response = await fetch(
      `http://localhost:8000/hackemate/user_transactions/${8}?format=month`
    )

    if (!response.ok) {
      return new Response("Error llamando al backend", { status: 500 })
    }

    const data = await response.json()

    return new Response(JSON.stringify(data), {
      status: 200,
      headers: {
        "Content-Type": "application/json",
      },
    })
  } catch (error) {
    return new Response(JSON.stringify({ error: String(error) }), {
      status: 500,
      headers: {
        "Content-Type": "application/json",
      },
    })
  }
}
