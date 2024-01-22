<template>
  <div class="contents">
    <!--<h1>{{ msg }}</h1> -->

    <div class="search-box">
      <div class="search-container">
        <img src="../assets/search.png" class="search-icon"></img>
        <input class="searchtext" type="text" placeholder="Type to search..." v-model="inputValue" @keyup.enter="select" />
      </div>
      <label for="search"> Search by: </label>
      <select id="search" v-model="selectedOption">
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
            <th>OWN-ID</th>
            <th>CVE-ID</th>
            <th>Date</th>
            <th>Title</th>
            <th>Bug-ID</th>
            <th>Author</th>
            <th>Software</th>
            <th>Platform</th>
          </tr>
        </thead>
        <tbody id="tableBody">
          <tr
            v-for="(item, index) in rows.slice((currentpage - 1) * 15, currentpage * 15)"
            :key="index"
            :class="{ 'odd-tr': (index + 1) % 2 === 1, 'even-tr': (index + 1) % 2 === 0 }"
          >
            <td>{{ item.own_ID }}</td>
            <td>{{ item.CVE_ID }}</td>
            <td>{{ item.time }}</td>
            <td>
              <router-link class="link" :to="{ name: 'Details', params: { item: item } }" >{{ item.title }}</router-link>
            </td>
            <td>{{ item.bugid }}</td>
            <td>{{ item.author }}</td>
            <td>{{ item.software_version }}</td>
            <td>{{ item.test_platform }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- 页数切换器 -->
    <ul class="pagination">
      <li><a @click="valdown">Previous</a></li>
      <li><input class="pagenum" type="text" v-model="pagenum" @keyup.enter="handleChangePage"/></li>
      <li><div>/  {{totalpage}}</div></li>
      <li><a @click="valup">Next</a></li>
    </ul>
    <div class="bottom-blank"></div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "Main",
  data() {
    return {
      currentpage: 1,
      totalpage: 100,
      resultnum: 100,
      inputValue: '',
      msg: "Welcome to CodeSecLab",
      pagenum: 1,
      rows: Array.from({ length: 15 }, (_, index) => ({
        'own_ID': 0,
        'author': '',
        'software_version': '',
      })),
      selectedOption: 'cve-id',
    };
  },
  methods: {
    handleChangePage() {
      if (this.pagenum > this.totalpage) {
        this.currentpage = this.totalpage;
        this.pagenum = this.totalpage;
      }
      else if (this.pagenum < 1) {
        this.currentpage = 1;
        this.pagenum = 1;
      }
      else {
        this.currentpage = this.pagenum;
      }
    },
    select() {
      console.log('new search');
      const FPath = 'http://localhost:5000';
      axios.post(FPath, {inputValue: this.inputValue, selectedOption: this.selectedOption})
                    .then((res) => {
                      console.log(res.data);
                      this.resultnum = res.data.length;
                      this.totalpage = Math.ceil(this.resultnum / 15);
                      this.rows = res.data;
                      //res为后端返回的查询数据
                    })
                    .catch((err) => {console.log(err)})
      
    },
    valdown() {
      if (this.currentpage > 1) {
        this.currentpage--;
        this.pagenum--;
      }
    },
    valup() {
      if (this.currentpage < this.totalpage) {
        this.currentpage++;
        this.pagenum++;
      }
    },
  },
  mounted() {
    this.select();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.bottom-blank {
  height: 10px;
}
.odd-tr {
  background-color: #ffffff;
}
.even-tr {
  background-color: #f2f2f2;
}
td .link {
  color: #001f3f;
  text-decoration: none;
}

td .link:hover {
  color: darkred;
  text-decoration: underline;
}
.search-container {
  position: relative;
  display: inline-block;
  
}

.search-icon {
  width: 4%;
  position: absolute;
  left: 13px; /* 调整图标距离左侧的位置 */
  top: 50%;
  transform: translateY(-50%);
  color: #888; /* 设置图标颜色 */
}

.pagination {
  font-size: 22px;
  margin-top: 30px;
  list-style: none;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}
.pagination li {
  margin-right: 20px;
}
.pagination a {
  text-decoration: none;
  color: #333;
  display: block;
}
.pagination a:hover {
  color: darkred;
}

.searchtext {
  border: 2px solid #ccc;
  height: 40px;
  width: 600px;
  font-size: 20px;
  margin-right: 15px;
  border-radius: 100px; /* 设置为足够大的值，根据需要调整 */
  padding: 10px; /* 可选：添加一些 padding 以增强样式 */
  padding-left: 50px;
  outline: none; /* 可选：去除输入框的默认轮廓样式 */
  transition: background-color 0.3s ease; /* 添加过渡效果 */
}
.searchtext:focus {
  border-color: #922d4f;
}
.searchtext:hover {
  background-color: #f0f0f0;
}
.pagenum{
  height: 40px;
  width: 45px;
  font-size: 20px;
  display: flex;
  align-items: center;
  text-align: center;
  border-radius: 5px;
  border: 2px solid #ccc;
  transition: background-color 0.3s ease;
}
.pagenum:focus {
  outline: 2px solid #922d4f;
}
.pagenum:hover {
  background-color: #f0f0f0;
}
tr {
  height: 40px;
}
/* 页数切换器容器样式 */

#search {
  height: 40px;
  font-size: 20px;
  padding: 5px;
  border-radius: 6px;
}
#search:hover{
  color: gray;
}
#search option{
  color: black;
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
#tableBody tr{
  height: 60px;
}
</style>
