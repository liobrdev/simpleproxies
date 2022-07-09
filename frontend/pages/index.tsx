import { Component } from 'react';

import Head from 'next/head';
import Link from 'next/link';
import { withRouter, NextRouter } from 'next/router';

import { IBreadcrumbListItem } from '@/types';


const apiUrl = process.env.NODE_ENV === 'development' ?
  'http://localhost:8000/api/proxies' : 'https://simpleproxies.app/proxies';


class Home extends Component<Props> {
  render() {
    const breadcrumbList: IBreadcrumbListItem[] = [
      {
        "@type": "ListItem",
        position: 1,
        name: "Home",
        item: "https://simpleproxies.app"
      }
    ];

    const breadcrumb = JSON.stringify({
      "@context": "https://schema.org/",
      "@type": "BreadcrumbList",
      "itemListElement": breadcrumbList
    });

    const year = new Date().getFullYear();

    return (
      <>
        <Head>
          <title>SimpleProxies</title>
          <script type="application/ld+json">{breadcrumb}</script>
        </Head>
        <main className='Page Page--home'>
          <p>
              Need a list of proxies for web scraping or other purposes?&nbsp;
              <b>free-proxy-list.net</b> is a great resource, but its web
              server does not have CORS headers configured to accept
              cross-origin requests. This shouldn&apos;t be a problem
              server-side, but when attempting a GET request on the client-side
              via web browser (e.g. a React.js component that fetches page
              info from free-proxy-list.net on button press) you&apos;ll likely
              be hit with an error informing you that your browser has
              blocked the request.
          </p>
          <p>
              So here&apos;s an alternative - a neat proxy server that will
              make the request for you! Cross-origin GET requests are
              allowed here, so instead of free-proxy-list.net, just have your
              client-side component make requests to the super simple
              API explained below. The server retrieves the
              payload from free-proxy-list.net without issue, then parses to
              a useful JSON format, and finally gets the proxies back to you.
          </p>
          <br/>
          <p className='Usage'>Usage</p>
          <table>
            <tbody>
              <tr>
                <td>
                  <Link href={apiUrl}>
                    <a>/proxies/</a>
                  </Link>
                  &nbsp;&nbsp;&nbsp;&nbsp;
                </td>
                <td>
                  Returns an array of &le; 100 elite/highly
                  anonymous SSL proxies
                </td>
              </tr>
            </tbody>
          </table>
          <div className='Footer Footer--home'>
            <div className='FooterLinks'><span>&copy; {year}</span></div>
          </div>
        </main>
      </>
    );
  }
}

interface Props {
  router: NextRouter;
}

export default withRouter(Home);
