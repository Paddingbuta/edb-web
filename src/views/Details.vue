<template>
  <div class="contents">
    <h1>{{ msg }}</h1>

    <div class="container">
      <div class="box">
        <h2 class="top-text">
          EDB-ID:
          <h3>51747</h3>
        </h2>
        <h2 class="top-text">
          CVE:
          <h3>2023-32707</h3>
        </h2>
        <hr />
        <div class="divider"></div>
        <div class="tp tp1">
          <h2 class="bottom-text">
            EDB Verified:
            <div class="pics"><img src="../assets/false.png" /></div>
          </h2>
        </div>
      </div>
      <div class="box">
        <h2 class="top-text">
          Author:
          <h3>REDWAY SECURITY</h3>
        </h2>
        <h2 class="top-text">
          Type:
          <h3>WEBAPPS</h3>
        </h2>
        <hr />
        <div class="divider"></div>
        <div class="tp tp2">
          <h2 class="bottom-text">
            Exploit:
            <div class="pics"><img src="../assets/download.png" /></div>
          </h2>
        </div>
      </div>
      <div class="box">
        <h2 class="top-text">
          Platform:
          <h3>MULTIPLE</h3>
        </h2>
        <h2 class="top-text">
          Date:
          <h3>2023-10-09</h3>
        </h2>
        <hr />
        <div class="divider"></div>
        <h2 class="bottom-text">Vulnerable App:</h2>
      </div>
    </div>
    <div class="bottom-blank"></div>
    <div class="code">
      <!-- Python 代码 -->
      <pre>
      <code class="language-python">
        {{ pythonCode }}
      </code>
    </pre>
    </div>

    <div class="bottom-blank"></div>
  </div>
</template>

<script>
import "prismjs/themes/prism.css";

export default {
  name: "Details",
  data() {
    return {
      msg: "OpenPLC WebServer 3 - Denial of Service",
      pythonCode: `
#!/usr/bin/env python3
#
# Exploit Title: Splunk 9.0.5 - admin account take over
# Author: [Redway Security](https://twitter.com/redwaysec))
# Discovery: [Santiago Lopez](https://twitter.com/santi_lopezz99)

#CVE: CVE-2023-32707

# Vendor Description: A low-privilege user who holds a role that has the capability assigned
# to it can escalate their privileges to that of the admin user by providing specially crafted web requests.
#
# Versions Affected: Splunk Enterprise **below** 9.0.5, 8.2.11, and 8.1.14.
#
import argparse
import requests
import random
import string
import base64
# ignore warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Splunk Authentication')
parser.add_argument('--host', required=True, help='Splunk host or IP address')
parser.add_argument('--username', required=True, help='Splunk username')
parser.add_argument('--password', required=True, help='Splunk password')
parser.add_argument('--target-user', required=True, help='Target user')
parser.add_argument('--force-exploit', action='store_true',
help='Force exploit')`,
    };
  },
};
</script>

<style>
.tp {
  display: flex;
  align-items: center;
  justify-content: center;
}
h2 {
  display: inline-block !important;
  margin: 10px 10px;
  height: 30px;
}
h3 {
  display: inline-block !important;
  font-size: 20px;
  color: #922d4f;
}
.language-python {
  padding: 0px 20px;
}
.tp1 img {
  width: 6%;
  height: 6%;
}
.tp2 img {
  width: 10%;
  height: 10%;
}
.code {
  display: flex;
  align-items: center;
  justify-content: center;
}
pre {
  background-color: #f5f0ee;
}
pre code {
  display: block;
  padding: 1em;
  overflow-x: auto;
  background-color: #282c34;
  color: #abb2bf;
  border-radius: 4px;
}
.contents {
  margin-top: 0px;
  margin: 0;
  text-align: center;
}
h1 {
  font-size: 40px;
  margin: 50px 0px;
}
.bottom-blank {
  height: 30px;
}
.container {
  display: flex;
  justify-content: center;
}

.box {
  width: 450px;
  height: 230px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f0f0f0;
  margin-right: 40px;
  border: 1px solid #ccc;
}

.divider {
  width: 100%;
  height: 1px;
  background-color: #ccc;
  margin: 10px 0;
}

/* 上方文字样式 */
.top-text {
  margin-bottom: 10px;
}

/* 下方文字样式 */
.bottom-text {
  margin-top: 10px;
}
</style>
