import { clerkMiddleware } from '@clerk/nextjs/server'
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

const ROUTES: Record<string, string> = {
  '/':         '/index.html',
  '/games':    '/games.html',
  '/groups':   '/groups.html',
  '/teams':    '/teams.html',
  '/my-team':  '/myteam.html',
  '/guide':    '/guide.html',
  '/bracket':  '/bracket.html',
  '/104-0':    '/draft.html',
}

export default clerkMiddleware((auth, request: NextRequest) => {
  const { pathname } = request.nextUrl
  const destination = ROUTES[pathname]
  if (destination) {
    const url = request.nextUrl.clone()
    url.pathname = destination
    return NextResponse.rewrite(url)
  }
})

export const config = {
  matcher: [
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    '/__clerk/:path*',
    '/(api|trpc)(.*)',
  ],
}
