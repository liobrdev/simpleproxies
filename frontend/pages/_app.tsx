import type { AppProps } from 'next/app';

import { RootComponent } from '@/components';

import '@/scss';


export default function App({ Component, pageProps }: AppProps) {
  return (
    <RootComponent>
      <Component {...pageProps} />
    </RootComponent>
  );
}