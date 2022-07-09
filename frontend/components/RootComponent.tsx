import React, { Component, ReactNode } from 'react';

import Head from 'next/head';


const description = (
  "Microservice to retrieve SSL proxies, " +
  "w/ CORS headers enabled to allow requests via browser."
);

class RootComponent extends Component<Props> {
  setAppHeight() {
    document.body.style.height = window.innerHeight + 'px';
  }

  componentDidMount() {
    window.addEventListener('resize', this.setAppHeight);
    this.setAppHeight();
  }

  componentWillUnmount() {
    window.removeEventListener('resize', this.setAppHeight);
  }

  render() {
    return (
      <>
        <Head>
          <meta charSet="utf-8" />
          <meta
            name="viewport"
            content="width=device-width, initial-scale=1"
          />
          <link
            rel="shortcut icon"
            type="image/x-icon"
            sizes="48x48"
            href="/favicon.ico"
          />
          <link
            rel="apple-touch-icon"
            type="image/png"
            sizes="180x180"
            href="/apple-touch-icon.png"
          />
          <link
            rel="icon"
            type="image/png"
            sizes="32x32"
            href="/favicon-32x32.png"
          />
          <link
            rel="icon"
            type="image/png"
            sizes="16x16"
            href="/favicon-16x16.png"
          />
          <link rel="manifest" href="/site.webmanifest" />
          <meta name="msapplication-TileColor" content="#4C7E4C" />
          <meta name="theme-color" content="#4C7E4C" />
          <meta itemProp="name" content="SimpleProxies" />
          <meta itemProp="description" content={description} />
          <meta name="description" content={description} />
          <meta property="og:title" content="SimpleProxies" />
          <meta property="og:type" content="website" />
          <meta property="og:url" content="https://simpleproxies.app/" />
          <meta property="og:description" content={description} />
        </Head>
        <div className='SiteContainer'>
          {this.props.children}
        </div>
      </>
    );    
  }
}

interface Props {
  children: ReactNode;
}

export default RootComponent;
