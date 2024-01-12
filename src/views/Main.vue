<template>
  <div class="contents">
    <!--<h1>{{ msg }}</h1> -->

    <div class="search-box">
      <input type="text" placeholder="  Type to search..." />
      <label for="search"> Search by: </label>
      <select id="search">
        <option value="cve-id">CVE-ID</option>
        <option value="title">Title</option>
        <option value="author">Author</option>
        <option value="software">Software</option>
        <option value="platform">Platform</option>
      </select>
    </div>

    <div>
      <table id="myTable">
        <thead>
          <tr>
            <th>Date</th>
            <th>Title</th>
            <th>Type</th>
            <th>Platform</th>
            <th>Author</th>
          </tr>
        </thead>
        <tbody id="tableBody">
          <tr
            v-for="(item, index) in rows"
            :key="index"
            :class="{ 'odd-tr': (index + 1) % 2 === 1, 'even-tr': (index + 1) % 2 === 0 }"
          >
            <td>{{ item.cell1 }}</td>
            <td>
              <router-link class="link" to="/details">{{ item.cell2 }}</router-link>
            </td>
            <td>{{ item.cell3 }}</td>
            <td>{{ item.cell4 }}</td>
            <td>{{ item.cell5 }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- 页数切换器 -->
    <ul class="pagination">
      <li><a href="#">Previous</a></li>
      <li class="current"><a href="#">1</a></li>
      <li><a href="#">2</a></li>
      <li><a href="#">3</a></li>
      <li><a href="#">4</a></li>
      <li><a href="#">5</a></li>
      <li>...</li>
      <li><a href="#">100</a></li>
      <li><a href="#">Next</a></li>
    </ul>
    <div class="bottom-blank"></div>
  </div>
</template>

<script>

export default {
  name: "Main",
  data() {
    return {
      msg: "Welcome to CodeSecLab",
      rows: Array.from({ length: 16 }, (_, index) => ({
        cell1: `2024-1-10`,
        cell2: `OpenPLC WebServer 3 - Denial of Service`,
        cell3: `DoS`,
        cell4: `Multiple`,
        cell5: `Kai Feng`,
      })),
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.bottom-blank {
  height: 10px;
}
.odd-tr {
  background-color: #f2f2f2;
}
.even-tr {
  background-color: #ffffff;
}
td .link {
  color: #001f3f;
  text-decoration: none;
}

td .link:hover {
  color: darkred;
  text-decoration: underline;
}
.pagination {
  margin-top: 30px;
  list-style: none;
  padding: 0;
  display: flex;
  justify-content: center;
}
.pagination li {
  display: inline-block;
  margin: 0 5px;
}
.pagination a {
  text-decoration: none;
  color: #333;
  display: block;
  padding: 8px 12px;
}
.pagination a:hover {
  background-color: #d0d0d0;
  border-radius: 50%;
}
.pagination .current a {
  background-color: orange;
  color: white;
}

input {
  height: 40px;
  width: 600px;
  font-size: 16px;
  margin-right: 15px;
}
tr {
  height: 40px;
}
/* 页数切换器容器样式 */

#search {
  height: 30px;
  font-size: 16px;
}

.search-box {
  top: 0;
  right: 0;
  margin-top: 20px;
  margin-right: 10px;
  margin-bottom: 20px;
  padding: 20px 20px;
  font-size: 20px;
}
table {
  border-collapse: collapse;
  width: 100%;
}

th,
td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: center;
}

th {
  background-color: #f2f2f2;
}
.contents {
  margin-top: 0px;
  margin: 0;
  text-align: center;
  font-size: 16px;
}
</style>
