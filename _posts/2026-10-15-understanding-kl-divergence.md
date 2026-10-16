---
layout: default
title: 理解 KL 散度
permalink: /blog/2026/understanding-kl-divergence/
date: 2026-10-15 12:00:00 +0800
lang: zh-CN
description: 从统计近似与信息论出发，理解 KL 散度、最大似然，以及正向与反向 KL 的差别。
excerpt: 从统计近似与信息论出发，理解 KL 散度、最大似然，以及正向与反向 KL 的差别。
article_kind: Machine learning
reading_time: 18
tags: [machine-learning, information-theory]
categories: [technical]
featured: false
math: true
---

{% capture article_body %}

<h2 id="definition">1 定义</h2>

设 $$P$$ 和 $$Q$$ 是定义在同一个样本空间上的两个概率分布。KL 散度（Kullback–Leibler divergence），也称相对熵，定义为：

$$
\boxed{
D_{\mathrm{KL}}(P\|Q)
=\sum_xp(x)\log\frac{p(x)}{q(x)}
}
$$

连续情况下，$$p,q$$ 表示概率密度，求和换成积分：

$$
\boxed{D_{\mathrm{KL}}(P\|Q)
=\int p(x)\log\frac{p(x)}{q(x)}\,dx
=\mathbb E_{X\sim P}\left[\log\frac{p(X)}{q(X)}\right]}
$$

离散与连续两种写法都可以统一写成期望：

$$
\boxed{D_{\mathrm{KL}}(P\|Q)
=\mathbb E_{X\sim P}\left[\log\frac{p(X)}{q(X)}\right]}
$$

### 基本性质

- **非负性**：$$D_{\mathrm{KL}}(P\|Q)\ge0$$，且仅在 $$P=Q$$ 时为零。
- **不对称性**：一般有 $$D_{\mathrm{KL}}(P\|Q)\ne D_{\mathrm{KL}}(Q\|P)$$。

离散情况下，$$p(x)=0$$ 的项记为零；若 $$p(x)>0$$ 而 $$q(x)=0$$，KL 为无穷大。

连续情况下，分布相同要求密度几乎处处相等，孤立点的差异不影响积分。

以下默认使用自然对数；信息论部分使用 $$\log_2$$，单位为 bit。

<h2 id="perspectives">2 理解视角</h2>

### 2.1 统计意义

设想我们进入一个矿洞，通过理想仪器扫描，得到了铁资源的真实空间分布 $$P$$。其中，$$x$$ 表示位置，$$p(x)$$ 是归一化后的资源密度，一个区域上的积分表示该区域占全部铁资源的比例。

矿洞通信不畅，只能传递少量参数。因此，我们与地面上的人约定：用一个高斯分布 $$Q_\theta$$ 近似资源分布，只传递它的均值和协方差。

问题是：**哪个高斯分布最适合代表这张资源地图？**

这里需要区分两种任务：

- **衡量差异**：给定 $$P,Q$$，评价它们相差多少。
- **寻找近似**：固定 $$P$$，在允许的分布中寻找最合适的 $$Q_\theta$$

需要注意的，这两个任务不是完全等价的，这也就是为什么KL散度不对称的原因。

当前关心的是第二种。真实分布是参照，高斯分布是近似，两者的角色不同。

我们需要评价的是：**哪一个参数对应的高斯分布最“适合“近似真实分布？**

最自然的想法是累计各处的绝对误差：

$$
\int|p(x)-q_\theta(x)|\,dx
$$

值得一提的是它的一半就是总变差距离（TV）

$$
\operatorname{TV}(P,Q)=\frac12\int|p(x)-q(x)|\,dx
$$

空间位置 $$x=(x_1,x_2,x_3)$$ 由三个坐标组成，其联合密度可分解为：

$$
p(x)=p(x_1)\,p(x_2\mid x_1)\,p(x_3\mid x_1,x_2)
$$

取对数，可以把这些累乘项转为累加：

$$
\log p(x)
=\log p(x_1)+\log p(x_2\mid x_1)+\log p(x_3\mid x_1,x_2)
$$

因此，我们考虑在对数空间中比较两种分布，用绝对值衡量位置 $$x$$ 处的偏差：

$$
\left|\log p(x)-\log q_\theta(x)\right|
=\left|\log\frac{p(x)}{q_\theta(x)}\right|
$$

回到矿洞场景：我们只能传递一个高斯分布，无法保留资源地图的全部细节，需要选择更准确地保留哪些区域的信息。很明显，我们希望高资源的区域能够精准传递，就可以用 $$p(x)$$ 对各处偏差加权，再对整个空间积分：

$$
\int p(x)\left|\log\frac{p(x)}{q_\theta(x)}\right|\,dx
$$

绝对值让每一处偏差都非负，但也使目标无法直接拆成两个平均对数项。

进一步考察会发现，不加绝对值的整体同样非负，而且仅在两个分布相同时为零，具体理由与证明在[附录 A](#appendix-a)。

$$
\boxed{
D_{\mathrm{KL}}(P\|Q_\theta)
=\int p(x)\log\frac{p(x)}{q_\theta(x)}\,dx
}
$$

因此，我们可以采用这个不带绝对值的指标，即 KL 散度。它还具有平均额外对数损失的解释

这保留了“有限信息下优先描述重要局部”的思路：在相同对数偏差下，真实概率质量越大的区域，贡献的绝对大小越大。但它不意味着只拟合一个峰，也不保证高斯的中心位于真实分布的最高峰。

KL 的方向性也体现在这里。$$D(P\|Q)$$ 按 $$P$$ 加权，评价用 $$Q$$ 近似 $$P$$的结果；交换之后，参照和权重都会改变，因此结果通常不同。两个角色不同允许我们采用有方向的评价，而 KL 的具体不对称性来自它的公式。

### 2.2 信息论

> 骰子的例子参考了[这篇 Quora 回答](https://qr.ae/pFmPVI)

熵衡量一个分布的不确定性。假设有两个骰子，公平骰子和真实骰子，公平骰子的六种结果同样可能，难以预测，熵较大；如果真实骰子几乎总是掷出 $$1$$，结果容易预测，熵就较小。

设骰子的真实分布为 $$P$$，它的熵是：

$$
H(P)=\sum_x p(x)\log_2\frac{1}{p(x)}.
$$

其中，$$\log_2\frac{1}{p(x)}$$ 表示结果 $$x$$ 发生时的意外程度：概率越小，发生时越意外。熵就是按实际发生频率计算的**平均意外程度**。

现在，真实骰子实际偏向点数 $$1$$，我们却误以为它是公平的。也就是说，真实分布是 $$P$$，我们采用的判断是 $$Q$$。

于是，每当频繁出现的 $$1$$ 被掷出，我们都会因为低估了它的概率而感到过于意外。其他点数则相反。将这些判断按实际发生频率平均，得到交叉熵：

$$
H(P,Q)=\sum_x p(x)\log_2\frac{1}{q(x)}.
$$

这里，$$p(x)$$ 决定结果实际出现多少次，$$q(x)$$ 决定我们认为这个结果有多意外。

**交叉熵减去真实分布的熵，就是使用错误判断所增加的平均意外程度，也就是 KL 散度：**

$$
\boxed{
D_{\mathrm{KL}}(P\|Q)
=H(P,Q)-H(P)
=\sum_x p(x)\log_2\frac{p(x)}{q(x)}.
}
$$

当 $$Q=P$$ 时，判断与真实分布一致，这部分额外代价为零。使用其他分布时，某些结果可能显得更容易预测，但按真实频率计算整体平均，交叉熵不会低于真实熵。

因此，KL 衡量的是采用另一分布进行判断的额外代价。骰子本身的不确定性仍由 $$H(P)$$ 决定，不会因为我们采用了 $$Q$$ 而改变。

<h2 id="machine-learning">3 机器学习中的 KL 散度</h2>

实际上在模型训练过程中，我们需要模型分布能够足够好的去拟合出真实分布，我们常常通过直接最小化KL散度来实现这一任务。

而最小化KL散度有意义是因为以下两点：

- KL 下降意味着平均对数预测损失下降

- KL 趋近零会保证分布在总变差意义下接近

具体的证明在[附录 B](#appendix-b)中。

KL散度是不对称的，对于分布$$P, Q_\theta$$，最小化$$D_{\mathrm{KL}}(P\|Q_\theta)$$与$$D_{\mathrm{KL}}(Q_\theta\|P)$$ 将会得到不同的结果。

### 3.1 从 KL 到最大似然

矿洞例子假设真实分布已知。机器学习中，我们通常只有来自真实分布的样本 $$x_1,\ldots,x_N\overset{\mathrm{i.i.d.}}{\sim}P$$，不知道 $$p(x)$$，希望训练模型 $$Q_\theta$$ 近似它。

正向 KL 可以展开为：

$$
D_{\mathrm{KL}}(P\|Q_\theta)
=\underbrace{\mathbb E_P[\log p(X)]}_{\text{与参数无关}}
-\mathbb E_P[\log q_\theta(X)]
$$

第一项不影响参数优化。用样本平均估计第二项，就得到训练损失：

$$
\boxed{
\widehat L(\theta)=-\frac1N\sum_{i=1}^N\log q_\theta(x_i)
}
$$

最小化它等价于最大化数据似然 $$\prod_iq_\theta(x_i)$$。因此，**即使不知道真实密度，也能通过最大似然估计，优化与正向 KL 对应的总体目标。** 这里要求模型的对数密度可计算，且上述期望分解有效。

分类中的交叉熵也是这个形式：对标签 $$y$$，单条样本的损失为 $$-\log q_\theta(y\mid x)$$。

相比之下，TV 的直接表达式包含 $$\lvert p(x)-q_\theta(x)\rvert$$，未知的真实密度无法分离成与参数无关的常数。TV 也能通过额外估计或判别方法优化，但没有这里直接转成样本对数似然的结构。

训练集损失只是总体损失的估计，下降不自动保证真实 KL 下降；模型表达能力有限时，最优 KL 也未必为零。最小化 KL 的意义与保证见[附录 B](#appendix-b)。

### 3.2 正向与反向 KL

两个方向都以 $$P=Q_\theta$$ 为理想最优解，但权重不同，模型受限时会选择不同的近似。

以两个相距较远、权重都显著的真实峰为例，模型仍然只能使用一个高斯：

- **正向 KL** 按 $$P$$ 取平均。两个峰都会产生真实样本，漏掉任何一峰都会造成较大的负对数损失，因此倾向于用较宽的高斯覆盖两峰。对于有限非零方差且相关期望有限的目标，最佳高斯匹配其均值与方差。
- **反向 KL** 按 $$Q_\theta$$ 取平均。较宽的高斯会在两峰之间生成样本，而那里真实密度低，代价较大，因此可能集中拟合其中一峰。目标中的负熵项又鼓励保留一定宽度，并非越窄越好。

计算上，反向 KL 为：

$$
D_{\mathrm{KL}}(Q_\theta\|P)
=\mathbb E_{Q_\theta}[\log q_\theta(X)-\log p(X)].
$$

其中 $$\mathbb E_{Q_\theta}[\log p(X)]$$ 随模型采样分布变化，不能作为常数删除。因此，只有真实样本时，通常不能像正向 KL 那样直接训练；能计算目标的未归一化密度时，则可用于变分推断。

<h2 id="appendix-a">附录 A 绝对值与非负性</h2>

**注意，KL 整体非负，不代表每一项非负。**

先设所有 $$p_i,q_i>0$$。由：

$$
\log u\le u-1,
$$

令 $$u=q_i/p_i$$，可得：

$$
p_i\log\frac{p_i}{q_i}\ge p_i-q_i.
$$

求和后：

$$
D_{\mathrm{KL}}(P\|Q)
\ge\sum_i(p_i-q_i)=0.
$$

等号要求每个 $$q_i/p_i=1$$，即 $$P=Q$$。

若存在 $$p_i=0$$，只对 $$S=\{i:p_i>0\}$$ 求和，有：

$$
D_{\mathrm{KL}}(P\|Q)\ge1-\sum_{i\in S}q_i\ge0.
$$

等号仍要求两个分布相同；（若 $$S$$ 中有 $$q_i=0$$，则 KL 为无穷大）

连续情况将求和换成积分即可。

因此，对有限 KL：

$$
\left|\sum_ip_i\log\frac{p_i}{q_i}\right|
=D_{\mathrm{KL}}(P\|Q),
$$

但一般有：

$$
\sum_ip_i\left|\log\frac{p_i}{q_i}\right|
\ne D_{\mathrm{KL}}(P\|Q).
$$

KL 保留正负贡献，是因为它衡量的是平均额外对数损失：

$$
D_{\mathrm{KL}}(P\|Q)
=\mathbb E_P[-\log q(X)]-\mathbb E_P[-\log p(X)].
$$

<h2 id="appendix-b">附录 B 为什么最小化 KL 有意义</h2>

“只有 $$P=Q$$ 时为零”只确定了正确零点，还不足以说明目标下降时分布如何变化。KL 另外具有两层保证。

**第一，KL 下降意味着平均对数预测损失下降。** 固定 $$P$$ 后：

$$
D_{\mathrm{KL}}(P\|Q)=H(P,Q)-H(P).
$$

$$H(P)$$ 是常数，所以 KL 每下降一单位，交叉熵也下降一单位。模型不能达到 $$P$$ 时，最小化 KL 仍是在模型集合中寻找平均对数损失最小的近似。

**第二，KL 趋近零会保证分布在总变差意义下接近。** 总变差距离满足：

$$
\operatorname{TV}(P,Q)
=\frac12\sum_x|p(x)-q(x)|
=\sup_A|P(A)-Q(A)|.
$$

它衡量两个分布对同一事件给出的概率最多能相差多少。使用自然对数时，Pinsker 不等式给出：

$$
\boxed{
\operatorname{TV}(P,Q)\le\sqrt{\frac12D_{\mathrm{KL}}(P\|Q)}.
}
$$

例如，KL 不超过 $$0.0002$$，则任意事件的概率误差都不超过 $$0.01$$。

不过，KL 下降只会降低这个上界，不保证实际 TV 每一步都下降。固定 $$P=(0.5,0.5,0)$$：

| 模型                     |     KL |   TV |
| ------------------------ | -----: | ---: |
| $$Q_1=(0.36,0.36,0.28)$$ | 0.3285 | 0.28 |
| $$Q_2=(0.8,0.2,0)$$      | 0.2231 | 0.30 |

从 $$Q_1$$ 到 $$Q_2$$，KL 减小，TV 却增大。因此，最小化 KL 有明确的预测意义和趋零保证，但不保证每一步改善所有分布距离或下游指标。

<h2 id="appendix-c">附录 C 更重视低概率的局部信息</h2>

可以改变评价标准，使罕见结果获得更大权重。但“更重视低概率结果”与“更严厉地惩罚严重低估”不同：KL 已经具有后者。对固定 $$p_i>0$$，无论它多小，当 $$q_i\to0$$ 时，$$p_i\log(p_i/q_i)\to+\infty$$。

若要额外提高某些结果的权重，可以使用加权对数损失：

$$
L_w(Q)=-\sum_ip_iw_i\log q_i,\qquad w_i>0.
$$

令 $$Z=\sum_ip_iw_i$$，$$\widetilde p_i=p_iw_i/Z$$，则 $$L_w(Q)=Z\,H(\widetilde P,Q)$$。因此，模型不受限制时：

$$
q_i^*=\frac{p_iw_i}{\sum_jp_jw_j}.
$$

它一般不再等于 $$P$$。例如，在所有 $$p_i>0$$ 的有限类别集合中，选择 $$w_i=1/p_i$$ 会使最优分布变成均匀分布。

若希望强调低概率位置，同时保留 $$P=Q$$ 为最优解，也可以考察加权平方误差，例如：

$$
D_\varepsilon(P,Q)=\sum_i\frac{(p_i-q_i)^2}{p_i+\varepsilon},\qquad\varepsilon>0.
$$

这个候选指标非负，仅在 $$P=Q$$ 时为零；相同绝对误差下，$$p_i$$ 越小，惩罚越大。但它需要知道真实概率，且依赖 $$\varepsilon$$ 的选择。

改变指标可以改变信息取舍。是否有用，需要检查它保留了什么性质、能否从样本估计；是否新颖，则需要针对具体公式判断，不能仅凭“不是 KL”得出结论。

{% endcapture %}

<link rel="stylesheet" href="{{ '/assets/css/home.css' | relative_url | bust_file_cache }}">

<div class="academic-home writing-detail-page writing-math-page">
  <a class="home-skip" href="#article-content">Skip to content</a>
  <header class="home-header">
    <a class="home-wordmark" href="{{ '/' | relative_url }}" aria-label="Leo (Xuling Zhao), home">{{ site.data.home.wordmark }}</a>
    <nav class="home-nav" aria-label="Main navigation">
      <a href="{{ '/' | relative_url }}">About</a>
      <a href="{{ '/publications/' | relative_url }}">Publications</a>
      <a href="{{ '/projects/' | relative_url }}">Projects</a>
      <a href="{{ '/blog/' | relative_url }}" aria-current="true">Writing</a>
      <a href="{{ '/notes/' | relative_url }}">Notes</a>
    </nav>
  </header>

  <article id="article-content" aria-labelledby="article-title" lang="{{ page.lang | default: site.lang }}">
    <header class="writing-detail-introduction">
      <a class="home-text-link" href="{{ '/blog/' | relative_url }}">← All writing</a>
      <p class="home-eyebrow">{{ page.article_kind }}</p>
      <h1 id="article-title">{{ page.title }}</h1>
      <p class="home-bio">{{ page.description }}</p>
      {% assign read_time = page.reading_time %}
      <p class="writing-meta"><time datetime="{{ page.date | date_to_xmlschema }}">{{ page.date | date: '%B %-d, %Y' }}</time> · {{ read_time }} min read</p>
    </header>

    {% if page.thumbnail %}
      <figure class="writing-cover">
        <img src="{{ page.thumbnail | relative_url }}" alt="{{ page.cover_alt | escape }}" width="1280" height="800" fetchpriority="high">
        <figcaption>{{ page.cover_caption }}</figcaption>
      </figure>
    {% endif %}

    <nav class="writing-contents" aria-label="文章目录" lang="zh-CN">
      <h2>本文目录</h2>
      <ol>
        <li><a href="#definition">1 定义</a></li>
        <li><a href="#perspectives">2 理解视角</a></li>
        <li><a href="#machine-learning">3 机器学习中的 KL 散度</a></li>
        <li><a href="#appendix-a">附录 A 绝对值与非负性</a></li>
        <li><a href="#appendix-b">附录 B 为什么最小化 KL 有意义</a></li>
        <li><a href="#appendix-c">附录 C 更重视低概率的局部信息</a></li>
      </ol>
    </nav>

    <div class="writing-prose">{{ article_body | markdownify }}</div>

    <div class="writing-tags writing-detail-tags" aria-label="Article topics">
      {% assign year = page.date | date: '%Y' %}
      <a href="{{ '/blog/archive/' | relative_url }}#year-{{ year }}">{{ year }}</a>
      {% for tag in page.tags %}<a href="{{ '/blog/archive/' | relative_url }}#tag-{{ tag | slugify }}">#{{ tag }}</a>{% endfor %}
      {% for category in page.categories %}<a href="{{ '/blog/archive/' | relative_url }}#category-{{ category | slugify }}">{{ category }}</a>{% endfor %}
    </div>

  </article>

  <nav class="writing-detail-navigation" aria-label="More writing">
    <a class="home-text-link" href="{{ '/blog/' | relative_url }}">← All writing</a>
    {% if page.next_article %}<a class="home-text-link" href="{{ page.next_article | relative_url }}">{{ page.next_article_title }} <span aria-hidden="true">↗</span></a>{% endif %}
  </nav>
  <footer class="home-footer"><span>© {{ site.time | date: '%Y' }} Xuling Zhao</span><span>Built with <a href="https://github.com/alshedivat/al-folio">al-folio</a></span></footer>
</div>
