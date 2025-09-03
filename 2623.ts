// https://leetcode.com/problems/memoize/description/


// # Memoize 函数分析与解决方案
//
// ## 问题评估
//
// 这个问题要求实现一个`memoize`函数，用于缓存函数调用的结果，避免重复计算。当使用相同参数再次调用函数时，直接返回缓存的结果而不执行原函数。
//
// ### 问题分析
//
// 1. 输入是一个函数`fn`，该函数接受任意数量的数字参数并返回一个数字
// 2. 返回值是一个新函数，行为与原函数相同，但会缓存结果
// 3. 当使用相同参数调用返回的函数时，应返回缓存结果而不调用原函数
//
// ### 边缘情况与约束
//
// 1. 参数数量可变（可以是任意数量的数字参数）
// 2. 需要考虑如何有效地创建缓存键（多个参数的情况）
// 3. 内存使用（长时间运行可能导致内存泄漏）
// 4. 参数顺序对结果的影响
//
// ## 解决方案
//
// ### 解决方案 1：使用参数数组字符串作为键
//
// ```typescript
type Fn = (...params: number[]) => number

function memoize(fn: Fn): Fn {
    const cache: Record<string, number> = {};

    return function (...args) {
        const key = JSON.stringify(args);
        if (key in cache) {
            return cache[key];
        }
        const result = fn(...args);
        cache[key] = result;
        return result;
    }
}

// ```
//
// **执行跟踪：**
//
// 假设我们有如下调用：
// ```typescript
// let callCount = 0;
// const memoizedFn = memoize(function (a, b) {
//     callCount += 1;
//     return a + b;
// });
// memoizedFn(2, 3); // 第一次调用
// memoizedFn(2, 3); // 第二次调用
// ```
//
// **调用栈跟踪：**
//
// 1. 初始化：创建一个空的`cache`对象，返回一个新函数
// 2. 第一次调用`memoizedFn(2, 3)`：
//    - 生成键：`key = JSON.stringify([2, 3]) = "[2,3]"`
//    - 检查`cache`中是否存在该键：不存在
//    - 调用原函数：`fn(2, 3)` 返回 `5`，`callCount` 变为 `1`
//    - 将结果存入缓存：`cache["[2,3]"] = 5`
//    - 返回结果：`5`
// 3. 第二次调用`memoizedFn(2, 3)`：
//    - 生成键：`key = JSON.stringify([2, 3]) = "[2,3]"`
//    - 检查`cache`中是否存在该键：存在
//    - 直接返回缓存结果：`cache["[2,3]"] = 5`，不调用原函数，`callCount` 保持为 `1`
//
// **边缘情况验证：**
//
// - 多参数情况：例如`memoizedFn(1, 2, 3)`，键将是`"[1,2,3]"`，缓存能正确工作
// - 参数顺序：`memoizedFn(2, 3)`和`memoizedFn(3, 2)`会有不同的键`"[2,3]"`和`"[3,2]"`，不会混淆
//
// **复杂度分析：**
//
// - 时间复杂度：查询缓存是O(1)，但JSON.stringify操作的复杂度取决于参数数量，约为O(n)，其中n是参数总长度
// - 空间复杂度：O(m)，其中m是不同参数组合的数量
//
// **优缺点：**
//
// 优点：
// - 实现简单直观
// - 能处理任意数量的参数
//
// 缺点：
// - JSON.stringify可能对于大型数组效率不高
// - 不能区分`[1,2]`和`["1","2"]`（在这个问题中不是问题，因为参数被类型定义为数字）
//
// ### 解决方案 2：使用Map和参数数组
//
// ```typescript
type Fn = (...params: number[]) => number

function memoize(fn: Fn): Fn {
    const cache = new Map<string, number>();

    return function (...args) {
        const key = args.toString();
        if (cache.has(key)) {
            return cache.get(key);
        }
        const result = fn(...args);
        cache.set(key, result);
        return result;
    }
}

// ```
//
// **执行跟踪：**
//
// 与解决方案1类似，但使用`Map`和`.toString()`来生成键。
//
// **边缘情况验证：**
//
// - 多参数情况：如`memoizedFn(1, 2, 3)`，键将是`"1,2,3"`
// - 参数顺序：`memoizedFn(2, 3)`和`memoizedFn(3, 2)`会有不同的键`"2,3"`和`"3,2"`
//
// **复杂度分析：**
//
// - 时间复杂度：O(n) 其中n是参数数量
// - 空间复杂度：O(m) 其中m是不同参数组合的数量
//
// **优缺点：**
//
// 优点：
// - 使用Map可能比简单对象效率更高
// - .toString()比JSON.stringify更简单
//
// 缺点：
// - .toString()可能在某些情况下产生冲突（例如,[1,2,3]和[1,2,3]会产生相同的字符串）但在此问题中参数是数字，所以问题较小
//
// ### 解决方案 3：递归生成唯一键
//
// ```typescript
type Fn = (...params: number[]) => number

function memoize(fn: Fn): Fn {
    const cache: Record<string, number> = {};

    return function (...args) {
        // 创建一个独特的键，用特殊字符分隔参数
        const key = args.map(arg => `${arg}:`).join('');
        if (key in cache) {
            return cache[key];
        }
        const result = fn(...args);
        cache[key] = result;
        return result;
    }
}

// ```
//
// **执行跟踪：**
//
// 类似前面的解决方案，但使用特殊分隔符来生成键。
//
// **边缘情况验证：**
//
// - 多参数情况：如`memoizedFn(1, 2, 3)`，键将是`"1:2:3:"`
// - 参数区分：`memoizedFn(1, 23)`和`memoizedFn(12, 3)`会有不同的键`"1:23:"`和`"12:3:"`，不会混淆
//
// **复杂度分析：**
//
// - 时间复杂度：O(n) 其中n是参数数量
// - 空间复杂度：O(m) 其中m是不同参数组合的数量
//
// **优缺点：**
//
// 优点：
// - 使用分隔符可以避免某些数字组合产生的歧义
// - 实现仍然相对简单
//
// 缺点：
// - 键生成方式比JSON.stringify更自制，可能有潜在边缘情况没考虑到
//
// ## 解决方案比较与选择
//
// | 解决方案 | 时间复杂度 | 空间复杂度 | 代码可读性 | 边缘情况处理 |
// |---------|-----------|-----------|-----------|------------|
// | 1. JSON.stringify | O(n) | O(m) | 高 | 良好 |
// | 2. Map + toString | O(n) | O(m) | 高 | 可能存在问题 |
// | 3. 特殊分隔符 | O(n) | O(m) | 中 | 良好 |
//
// **最优解决方案：解决方案1**
//
// 我选择解决方案1作为最优方案，主要基于以下考虑：
//
// 1. **编码面试适用性**：代码简洁明了，容易在面试中编写和解释
// 2. **时间和空间复杂度**：与其他解决方案相当
// 3. **代码可读性**：使用JSON.stringify是处理JS/TS中复杂键的标准做法，容易理解
// 4. **边缘情况处理**：JSON.stringify能正确处理所有数字参数组合，不会有歧义
//
// 实际开发环境中，可能需要考虑内存限制和长期缓存问题，但对于面试问题，解决方案1提供了清晰、简洁且正确的实现。
