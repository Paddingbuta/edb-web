<template>
  <div class="contents">
    <h1>{{ item.title }}</h1>

    <div class="container">
      <div class="box3">
        <h2 class="top-text ownid">
          OWN-ID:
          <h3>{{item.own_ID}}</h3>
        </h2>
        <h2 class="top-text">
          CVE-ID:
          <h3>{{item.CVE_ID}}</h3>
        </h2>
      </div>
      <div class="box">
        <h2 class="top-text">
          Test Platform:
          <h3>{{item.test_platform}}</h3>
        </h2>
        <h2 class="top-text">
          Software Version:
          <h3>{{item.software_version}}</h3>
        </h2>
        <h2 class="top-text">
          Tag: <h3>{{item.tag}}</h3>  Code Language:
          <h3>{{item.code_language}}</h3>
        </h2>
      </div>
      <div class="box">
        <h2 class="top-text">
          Author:
          <h3>{{item.author}}</h3>
        </h2>
        <h2 class="top-text">
          Source:
          <h3>{{item.source}}</h3>
        </h2>
        <h2 class="top-text">
          Time:
          <h3>{{item.time}}</h3>
        </h2>
      </div>
    </div>
    <div class="bottom-blank"></div>
    <div class="container">
      <div class="box2">
        <h2 class="top-text">
          Reference:
          <h3>{{item.reference}}</h3>
        </h2>
      </div>
    </div>
    <div class="bottom-blank"></div>
    <div class="container">
      <div class="box2">
        <h2 class="top-text">
          Trigger Method:
          <h3>{{item.trigger_method}}</h3>
        </h2>
      </div>
    </div>
    <div class="bottom-blank"></div>
    <div class="container">
      <div class="box2">
        <h2 class="top-text">
          Record:
          <h3>{{item.record}}</h3>
        </h2>
      </div>
    </div>
    <div class="bottom-blank"></div>
    <div class="code">
      <!-- Python 代码 -->
      <pre>
      <code class="language-python">
        {{item.other_information}}
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
  created() {
    this.item = this.$route.params.item;
    this.item.other_information = JSON.parse(this.item.other_information);
  },
  data() {
    return {
      item: null,
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
h2 {
  display: inline-block !important;
  margin: 20px 10px;
  height: 30px;
}
h2.ownid{
  margin-top: 0px;
}
h3 {
  display: inline-block !important;
  font-size: 20px;
  color: #922d4f;
}
.language-python {
  width: 1000px;
  padding: 0px 20px;
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
  width: 500px;
  height: 220px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f0f0f0;
  margin-right: 40px;
  border: 1px solid #ccc;
}

.box2 {
  width: 1435px;
  height: 100px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f0f0f0;
  margin-right: 40px;
  border: 1px solid #ccc;
}

.box3 {
  width: 450px;
  height: 220px;
  display: flex;
  justify-content: center;
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

</style>
